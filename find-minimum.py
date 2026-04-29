import math

def find_minimum(lst):
    minimum = math.inf
    
    for item in lst:
        if item < minimum:
            minimum = item
            
    return minimum


def find_minimum_v2(lst):
    lst.sort()
    return lst[0]


if __name__ == "__main__":
    result = find_minimum_v2([1,-2,1,2,-10])
    print(result)