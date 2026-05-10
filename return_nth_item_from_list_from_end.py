

lst = [1,2,3,4,5,6,7,8]


def findNthElementFromEnd(array,nth):
    result = 0
    end = result + nth
    
    while end < len(array):
        end = end + 1
        result = result + 1
        
    return array[result]


if __name__ == "__main__":
    result = findNthElementFromEnd(lst, 1)
    print(result)