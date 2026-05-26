import pytest
from graph_impl import Graph, breadth_first_search, depth_first_search, detect_cycle_in_graph


# ─── helpers ───────────────────────────────────────────────────────────────────

def make_graph(edges: list[tuple[str, str]], nodes: list[str] | None = None) -> Graph:
    """Build a graph from an edge list. Infers nodes if not supplied."""
    if nodes is None:
        seen = []
        for src, dst in edges:
            if src not in seen:
                seen.append(src)
            if dst not in seen:
                seen.append(dst)
        nodes = seen
    g = Graph(nodes[:])
    for src, dst in edges:
        g.add_neighbour(src, dst)
    return g


# ─── BFS ───────────────────────────────────────────────────────────────────────

class TestBFS:

    # ── basic correctness ──────────────────────────────────────────────────────

    def test_single_node(self):
        g = Graph(["A"])
        assert breadth_first_search(g, "A") == ["A"]

    def test_two_nodes_connected(self):
        g = make_graph([("A", "B")])
        assert breadth_first_search(g, "A") == ["A", "B"]

    def test_two_nodes_disconnected(self):
        g = Graph(["A", "B"])
        assert breadth_first_search(g, "A") == ["A"]

    def test_linear_chain(self):
        # A → B → C → D → E
        g = make_graph([("A","B"),("B","C"),("C","D"),("D","E")])
        assert breadth_first_search(g, "A") == ["A","B","C","D","E"]

    def test_simple_graph_from_spec(self):
        nodes = ["A","B","C","D","E","F","G","H"]
        g = Graph(nodes[:])
        for src, dst in [
            ("A","B"),("A","C"),("A","D"),("A","E"),
            ("B","F"),("C","F"),("D","F"),("E","F"),
            ("F","G"),("F","H"),("G","H"),
        ]:
            g.add_neighbour(src, dst)
        assert breadth_first_search(g, "A") == ["A","B","C","D","E","F","G","H"]

    # ── level-order guarantee ──────────────────────────────────────────────────

    def test_bfs_visits_level_by_level(self):
        #     A
        #    / \
        #   B   C
        #  / \   \
        # D   E   F
        g = make_graph([("A","B"),("A","C"),("B","D"),("B","E"),("C","F")])
        result = breadth_first_search(g, "A")
        assert result.index("A") < result.index("B")
        assert result.index("A") < result.index("C")
        assert result.index("B") < result.index("D")
        assert result.index("B") < result.index("E")
        assert result.index("C") < result.index("F")

    def test_bfs_wide_root(self):
        # A fans out to B,C,D,E,F — all are level-1, G is level-2 via B
        g = make_graph([("A","B"),("A","C"),("A","D"),("A","E"),("A","F"),("B","G")])
        result = breadth_first_search(g, "A")
        assert result[0] == "A"
        assert result.index("G") > result.index("B")
        assert result.index("G") > result.index("C")

    # ── cycle handling ─────────────────────────────────────────────────────────

    def test_cycle_does_not_loop_forever(self):
        # A → B → A (direct cycle)
        g = make_graph([("A","B"),("B","A")])
        result = breadth_first_search(g, "A")
        assert result == ["A","B"]

    def test_self_loop(self):
        g = make_graph([("A","A"),("A","B")])
        result = breadth_first_search(g, "A")
        assert result.count("A") == 1

    def test_triangle_cycle(self):
        g = make_graph([("A","B"),("B","C"),("C","A")])
        result = breadth_first_search(g, "A")
        assert sorted(result) == ["A","B","C"]
        assert result.count("A") == 1

    def test_complex_cycle_from_spec(self):
        nodes = ["A","B","C","D","E","F","G","H"]
        g = Graph(nodes[:])
        for src, dst in [
            ("A","B"),("A","C"),("A","D"),("A","E"),
            ("B","F"),("C","F"),("D","F"),("E","F"),
            ("E","A"),                              # back-edge
            ("F","G"),("F","H"),("G","H"),
        ]:
            g.add_neighbour(src, dst)
        result = breadth_first_search(g, "A")
        assert result == ["A","B","C","D","E","F","G","H"]
        assert result.count("A") == 1

    def test_multiple_back_edges(self):
        g = make_graph([
            ("A","B"),("A","C"),
            ("B","D"),("C","D"),
            ("D","A"),("D","B"),   # two back-edges
        ])
        result = breadth_first_search(g, "A")
        assert sorted(result) == ["A","B","C","D"]
        for node in ["A","B","C","D"]:
            assert result.count(node) == 1

    # ── disconnected components ────────────────────────────────────────────────

    def test_disconnected_component_not_reached(self):
        g = Graph(["A","B","C","D"])
        g.add_neighbour("A","B")
        g.add_neighbour("C","D")   # separate component
        result = breadth_first_search(g, "A")
        assert "C" not in result
        assert "D" not in result

    def test_start_from_isolated_node(self):
        g = Graph(["A","B","C"])
        g.add_neighbour("B","C")
        result = breadth_first_search(g, "A")
        assert result == ["A"]

    # ── directed-edge semantics ────────────────────────────────────────────────

    def test_directed_one_way(self):
        # A → B but NOT B → A
        g = make_graph([("A","B")])
        assert "A" not in breadth_first_search(g, "B")

    def test_directed_asymmetric_reachability(self):
        g = make_graph([("A","B"),("A","C"),("B","D")])
        from_a = breadth_first_search(g, "A")
        from_d = breadth_first_search(g, "D")
        assert sorted(from_a) == ["A","B","C","D"]
        assert from_d == ["D"]

    # ── large / stress ─────────────────────────────────────────────────────────

    def test_long_chain_100_nodes(self):
        nodes = [str(i) for i in range(100)]
        edges = [(str(i), str(i+1)) for i in range(99)]
        g = make_graph(edges, nodes)
        result = breadth_first_search(g, "0")
        assert result == nodes

    def test_star_graph_50_leaves(self):
        leaves = [str(i) for i in range(50)]
        nodes = ["center"] + leaves
        g = Graph(nodes[:])
        for leaf in leaves:
            g.add_neighbour("center", leaf)
        result = breadth_first_search(g, "center")
        assert result[0] == "center"
        assert sorted(result[1:]) == sorted(leaves)

    def test_complete_graph_5_nodes(self):
        nodes = ["A","B","C","D","E"]
        g = Graph(nodes[:])
        for src in nodes:
            for dst in nodes:
                if src != dst:
                    g.add_neighbour(src, dst)
        result = breadth_first_search(g, "A")
        assert sorted(result) == nodes
        for n in nodes:
            assert result.count(n) == 1


# ─── DFS ───────────────────────────────────────────────────────────────────────

class TestDFS:

    # ── basic correctness ──────────────────────────────────────────────────────

    def test_single_node(self):
        g = Graph(["A"])
        assert depth_first_search(g, "A") == ["A"]

    def test_two_nodes_connected(self):
        g = make_graph([("A","B")])
        assert depth_first_search(g, "A") == ["A","B"]

    def test_two_nodes_disconnected(self):
        g = Graph(["A","B"])
        assert depth_first_search(g, "A") == ["A"]

    def test_linear_chain(self):
        g = make_graph([("A","B"),("B","C"),("C","D"),("D","E")])
        result = depth_first_search(g, "A")
        assert sorted(result) == ["A","B","C","D","E"]

    # ── depth-first ordering guarantee ────────────────────────────────────────

    def test_dfs_goes_deep_before_wide(self):
        #     A
        #    / \
        #   B   C
        #   |
        #   D
        # Contract: whichever branch DFS takes first, it must finish
        # that entire branch before visiting nodes on the other branch.
        g = make_graph([("A","B"),("A","C"),("B","D")])
        result = depth_first_search(g, "A")

        assert result[0] == "A"
        # D is only reachable through B — so D must come after B
        assert result.index("B") < result.index("D")
        # C is a sibling of B — DFS must finish the B→D branch before C
        # meaning: whichever of B or C appears first, D must appear before the other
        b_idx, c_idx, d_idx = result.index("B"), result.index("C"), result.index("D")
        if b_idx < c_idx:
            assert d_idx < c_idx, "DFS took B branch first but visited C before finishing it"
        else:
            assert b_idx < d_idx  # sanity: B always before D


    def test_dfs_ordering_deep_path(self):
        # A → B → C → D, and A → E
        # Contract: DFS must fully exhaust the path it takes first.
        # If it goes A→B, it must reach D before touching E.
        # If it goes A→E first, E appears before B,C,D.
        g = make_graph([("A","B"),("B","C"),("C","D"),("A","E")])
        result = depth_first_search(g, "A")

        assert result[0] == "A"
        b_idx, e_idx = result.index("B"), result.index("E")
        if b_idx < e_idx:
            # took the B branch first — must finish B→C→D before E
            assert result.index("C") < e_idx
            assert result.index("D") < e_idx
        else:
            # took E first — E appears before B,C,D
            assert e_idx < b_idx
        
    
    # ── the bug in the impl ────────────────────────────────────────────────────

    def test_catches_hardcoded_source_bug(self):
        """
        The impl checks get_vertex_neighbours(source) instead of
        get_vertex_neighbours(vertex) when deciding whether to push neighbours.
        On this graph, starting from A, once we pop B the neighbour-check
        runs on 'A' (the original source) not 'B' — so C is never pushed.
        """
        g = make_graph([("A","B"),("B","C"),("C","D")])
        result = depth_first_search(g, "A")
        assert "C" in result, (
            "Bug: neighbours of intermediate vertices are never explored "
            "because the impl checks source instead of vertex"
        )
        assert "D" in result

    def test_catches_bug_multi_branch(self):
        """Same bug — from A, only A's direct neighbours survive the check."""
        g = make_graph([("A","B"),("B","D"),("B","E"),("A","C"),("C","F")])
        result = depth_first_search(g, "A")
        assert sorted(result) == ["A","B","C","D","E","F"], (
            f"Expected all 6 nodes, got {result}"
        )

    # ── cycle handling ─────────────────────────────────────────────────────────

    def test_cycle_does_not_loop_forever(self):
        g = make_graph([("A","B"),("B","A")])
        result = depth_first_search(g, "A")
        assert sorted(result) == ["A","B"]
        assert result.count("A") == 1

    def test_self_loop(self):
        g = make_graph([("A","A"),("A","B")])
        result = depth_first_search(g, "A")
        assert result.count("A") == 1

    def test_triangle_cycle(self):
        g = make_graph([("A","B"),("B","C"),("C","A")])
        result = depth_first_search(g, "A")
        assert sorted(result) == ["A","B","C"]
        for n in ["A","B","C"]:
            assert result.count(n) == 1

    def test_complex_cycle(self):
        g = make_graph([
            ("A","B"),("A","C"),("B","D"),
            ("C","D"),("D","A"),("D","B"),
        ])
        result = depth_first_search(g, "A")
        assert sorted(result) == ["A","B","C","D"]
        for n in ["A","B","C","D"]:
            assert result.count(n) == 1

    # ── disconnected components ────────────────────────────────────────────────

    def test_disconnected_component_not_reached(self):
        g = Graph(["A","B","C","D"])
        g.add_neighbour("A","B")
        g.add_neighbour("C","D")
        result = depth_first_search(g, "A")
        assert "C" not in result
        assert "D" not in result

    def test_start_from_isolated_node(self):
        g = Graph(["A","B","C"])
        g.add_neighbour("B","C")
        assert depth_first_search(g, "A") == ["A"]

    # ── directed-edge semantics ────────────────────────────────────────────────

    def test_directed_one_way(self):
        g = make_graph([("A","B")])
        assert "A" not in depth_first_search(g, "B")

    def test_directed_asymmetric_reachability(self):
        g = make_graph([("A","B"),("A","C"),("B","D")])
        from_a = depth_first_search(g, "A")
        from_d = depth_first_search(g, "D")
        assert sorted(from_a) == ["A","B","C","D"]
        assert from_d == ["D"]

    # ── all nodes visited exactly once ─────────────────────────────────────────

    def test_each_node_visited_once(self):
        g = make_graph([
            ("A","B"),("A","C"),("B","D"),("B","E"),
            ("C","E"),("D","F"),("E","F"),
        ])
        result = depth_first_search(g, "A")
        assert len(result) == len(set(result)), "Duplicate nodes in DFS output"

    # ── large / stress ─────────────────────────────────────────────────────────

    def test_long_chain_100_nodes(self):
        nodes = [str(i) for i in range(100)]
        edges = [(str(i), str(i+1)) for i in range(99)]
        g = make_graph(edges, nodes)
        result = depth_first_search(g, "0")
        assert sorted(result) == sorted(nodes)

    def test_star_graph_50_leaves(self):
        leaves = [str(i) for i in range(50)]
        nodes = ["center"] + leaves
        g = Graph(nodes[:])
        for leaf in leaves:
            g.add_neighbour("center", leaf)
        result = depth_first_search(g, "center")
        assert result[0] == "center"
        assert sorted(result[1:]) == sorted(leaves)

    def test_complete_graph_5_nodes(self):
        nodes = ["A","B","C","D","E"]
        g = Graph(nodes[:])
        for src in nodes:
            for dst in nodes:
                if src != dst:
                    g.add_neighbour(src, dst)
        result = depth_first_search(g, "A")
        assert sorted(result) == nodes
        for n in nodes:
            assert result.count(n) == 1


# ─── BFS vs DFS contract ───────────────────────────────────────────────────────

class TestBFSvsDFS:

    def test_both_visit_same_nodes_simple(self):
        g = make_graph([("A","B"),("A","C"),("B","D"),("C","D")])
        assert sorted(breadth_first_search(g,"A")) == sorted(depth_first_search(g,"A"))

    def test_both_visit_same_nodes_with_cycle(self):
        g = make_graph([("A","B"),("B","C"),("C","A"),("C","D")])
        assert sorted(breadth_first_search(g,"A")) == sorted(depth_first_search(g,"A"))

    def test_order_differs_on_branching_graph(self):
        #     A
        #    / \
        #   B   C
        #   |
        #   D
        # BFS: A B C D   DFS: A B D C  (or A C B D depending on stack order)
        g = make_graph([("A","B"),("A","C"),("B","D")])
        bfs = breadth_first_search(g,"A")
        dfs = depth_first_search(g,"A")
        assert sorted(bfs) == sorted(dfs)   # same nodes
        assert bfs != dfs                   # different order

    def test_single_node_both_agree(self):
        g = Graph(["Z"])
        assert breadth_first_search(g,"Z") == depth_first_search(g,"Z") == ["Z"]
        

class TestDetectCycleInGraph:
    def test_no_cycle_detection(self):
        g = make_graph([("A","B"),("A","C"),("B","D"),("C","D")])
        cycle_detected = detect_cycle_in_graph(g)
        assert cycle_detected == False
    
    def test_cycle_detection_with_given_cycle_graph(self):
        g = Graph(["A","B","C","D","E","X","Y","O"])
        g.add_neighbour("A","B")
        g.add_neighbour("A","C")
        g.add_neighbour("A","D")
        g.add_neighbour("B","E")
        g.add_neighbour("C","E")
        g.add_neighbour("D","E")
        g.add_neighbour("E","X")
        g.add_neighbour("X","Y")
        g.add_neighbour("Y","D")
        g.add_neighbour("D","O")
        g.add_neighbour("O","A")
        g.add_neighbour("A","O")
        cycle_detected = detect_cycle_in_graph(g)
        assert cycle_detected == True