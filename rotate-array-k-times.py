# The tricky part is when we have duplicated entries
# So that's why i had to come up with copied container
def right_rotate(nums, k):
    output = []
    output[:] = nums[:]
    for i in range(len(nums)):
        if (i + k) >= len(nums):
            index_to_live_at = i + k - len(nums)
            while index_to_live_at >= len(nums):
                index_to_live_at = index_to_live_at - len(nums)
            output[index_to_live_at] = nums[i] 
        else:
            corrected_idx = i + k
            output[corrected_idx] = nums[i]
    return output


if __name__ == "__main__":
    results = right_rotate([2,2,1,1,4,5], 2)
    print(results)
    