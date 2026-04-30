def find_second_maximum(nums):
    first_max = second_max = float('-inf')
   
    for i in range(len(nums)):
        if (nums[i] > first_max):
            second_max = first_max
            first_max = nums[i]
       
        # If the current number is greater than the second maximum and not equal to first_max
        elif (nums[i] != first_max and nums[i] > second_max):
            second_max = nums[i]
   
    return second_max



if __name__ == "__main__":
    output = find_second_maximum([4,-2,5,-2,5,6])
    print(output)