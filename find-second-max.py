def find_second_maximum(nums):
    slow = 0
    fast = 1
    
    detected_max = max(nums[slow], nums[fast])
    second_max = min(nums[slow], nums[fast])
    
    slow = slow + 1
    fast = fast + 1
    
    while fast < len(nums):
        cal_max = max(nums[slow], nums[fast])
        if cal_max > detected_max:
            second_max = detected_max
            detected_max = cal_max
        
        if cal_max > second_max and cal_max < detected_max:
            second_max = cal_max
            
        slow = slow + 1
        fast = fast + 1
    
    return second_max


if __name__ == "__main__":
    output = find_second_maximum([4,-2,5,-2,5,6])
    print(output)