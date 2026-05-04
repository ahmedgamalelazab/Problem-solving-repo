# find max subarray 
# The problem is dynamic programming based


def find_max_sum_sublist(nums):
    db = nums[:]
    max_sum = db[0]
    for i in range(1, len(nums)):
        db[i] = max(nums[i], (db[i-1] + nums[i]))
        max_sum = max(max_sum, db[i])
    return max_sum


if __name__ == "__main__":
    inputs = [[1, 2, 2, 3, 3, 1, 4], [2, 2, 1], [4, 1, 2, 1, 2], [-4, -1, -2, -1, -2],[-4, 2, -5, 1, 2, 3, 6, -5, 1], [25]]
    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\tMaximum Sum: ", find_max_sum_sublist(inputs[i]), sep="")
        print("-" * 75)