def find_first_unique(nums):
    # store the frequency of the nums after scan them
    scan_freq = {}
    for item in nums:
        if item in scan_freq:
            scan_freq[item] = scan_freq[item] + 1
        else:
            scan_freq[item] = 1
    
    for item in nums:
        if item in scan_freq and scan_freq[item] == 1:
            return item
    # Replace this placeholder return statement with your code
    return -1


if __name__ == "__main__":
    result = find_first_unique([1,1,1,2,3,3,4,5,5,6,6,7])
    print(result)