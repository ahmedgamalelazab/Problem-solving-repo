from functools import reduce

# first we need to know how many zeros in our incoming array
def scan_zeros(arr):
    scan_results = {"counts": 0, "indexes": []}
    for i in range(len(arr)):
        if arr[i] == 0:
            scan_results["counts"] = scan_results["counts"] + 1
            scan_results["indexes"].append(i)
    return scan_results

# define a product of nums, the logic support to assume no zeros in the code
# warning don't use this unless we know that the codebase
# the following function will skip zeros to be valid product in case we found 1 zero in the list
def calc_product_of_arr(arr):
    return reduce(lambda x,y: (x if x != 0 else 1) * (y if y != 0 else 1), arr)
    


def find_product(nums):
    count_for_zeros_results = scan_zeros(nums)
    
    if count_for_zeros_results["counts"] == 0:
        product_of_all = calc_product_of_arr(nums)
        for i in range(len(nums)):
            nums[i] = int(product_of_all / nums[i])
        return nums
    elif count_for_zeros_results["counts"] == 1:
        product_of_all = calc_product_of_arr(nums)
        nums = list(map(lambda item: 0 if item != 0 else item, nums))
        nums[count_for_zeros_results["indexes"][0]] = product_of_all
        return nums
    else:
        # else means the counts exceed the 1
        return list(map(lambda item: 0 if item >= 0 else item, nums))
    
    
    
if __name__ == "__main__":
    result = find_product([1, 1, 2, 0])
    print(result)