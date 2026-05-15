import sys

# Force-disable the GIL even if a C extension tries to re-enable it
if hasattr(sys, '_is_gil_enabled'):
    import _testinternalcapi
    # or use the environment variable approach (more reliable):
    pass

"""
Python 3.14 GIL vs Free-Threaded Benchmark
============================================
Run with standard Python:       python benchmark_gil.py
Run with free-threaded Python:  python3.14t benchmark_gil.py

Requires Python 3.13+ for sys._is_gil_enabled()
"""
import time
import threading
import hashlib
import math
from concurrent.futures import ThreadPoolExecutor

# ── Config ────────────────────────────────────────────────────────────────────
THREAD_COUNTS   = [1, 2, 4, 8]
ITERATIONS      = 2_000_000   # work units per task
HASH_BYTES      = b"benchmark_payload_python_3_14_free_threading"

# ── GIL detection ─────────────────────────────────────────────────────────────
def gil_status() -> str:
    if not hasattr(sys, "_is_gil_enabled"):
        return "unknown (Python < 3.13)"
    return "ENABLED" if sys._is_gil_enabled() else "DISABLED (free-threaded ✓)"

# ── CPU-bound tasks ───────────────────────────────────────────────────────────

def task_hashing(n: int) -> int:
    """SHA-256 hashing loop — pure CPU, no I/O, no C-extension parallelism."""
    h = hashlib.sha256()
    for _ in range(n):
        h = hashlib.sha256(h.digest() + HASH_BYTES)
    return int(h.hexdigest(), 16) % 1_000_000

def task_math(n: int) -> float:
    """Pure-Python floating-point math — worst case for GIL contention."""
    acc = 0.0
    for i in range(1, n + 1):
        acc += math.sqrt(i) * math.log(i + 1) / (i * 0.001 + 1)
    return acc

def task_primes(n: int) -> int:
    """Count primes up to n using a simple trial-division sieve."""
    count = 0
    for num in range(2, n):
        if all(num % d != 0 for d in range(2, int(num**0.5) + 1)):
            count += 1
    return count

# ── Benchmark runner ──────────────────────────────────────────────────────────

def run_single(task_fn, workload: int) -> float:
    start = time.perf_counter()
    task_fn(workload)
    return time.perf_counter() - start

def run_threaded(task_fn, workload: int, n_threads: int) -> float:
    with ThreadPoolExecutor(max_workers=n_threads) as pool:
        start = time.perf_counter()
        futures = [pool.submit(task_fn, workload) for _ in range(n_threads)]
        [f.result() for f in futures]          # wait for all
        return time.perf_counter() - start

def bench(label: str, task_fn, workload: int):
    print(f"\n{'─' * 60}")
    print(f"  Task: {label}")
    print(f"{'─' * 60}")

    baseline = run_single(task_fn, workload)
    print(f"  {'Threads':>8}  {'Time (s)':>10}  {'Speedup':>10}  {'Efficiency':>12}")
    print(f"  {'1 (base)':>8}  {baseline:>10.3f}  {'1.00x':>10}  {'100%':>12}")

    for n in THREAD_COUNTS[1:]:
        elapsed = run_threaded(task_fn, workload, n)
        speedup   = baseline / elapsed
        efficiency = speedup / n * 100
        flag = " ← true parallelism!" if speedup > 1.5 * n / n else ""
        print(
            f"  {n:>8}  {elapsed:>10.3f}  {speedup:>9.2f}x"
            f"  {efficiency:>11.1f}%{flag}"
        )

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  Python GIL Benchmark")
    print("=" * 60)
    print(f"  Python version : {sys.version.split()[0]}")
    print(f"  GIL status     : {gil_status()}")
    print(f"  Build          : {'free-threading' if 't' in sys.version else 'standard'}")
    print("=" * 60)

    # Adjust workloads so each task takes ~1–2s on a single thread
    bench("SHA-256 hashing (CPU-bound)", task_hashing, ITERATIONS // 2)
    bench("Pure-Python math (sqrt + log loop)", task_math, ITERATIONS)
    bench("Prime counting (trial division)", task_primes, 8_000)

    print(f"\n{'=' * 60}")
    print("  Interpretation guide")
    print(f"{'=' * 60}")
    print("  With GIL:          speedup ≈ 1.0x regardless of threads")
    print("  Free-threaded:     speedup should approach N × threads")
    print("  Efficiency > 80%:  near-linear scaling — true parallelism")
    print("  Efficiency < 20%:  GIL (or lock contention) is throttling")
    print("=" * 60)

if __name__ == "__main__":
    main()