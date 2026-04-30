# What we learnt here, that in python we never reach the end of our last index
# In example if we loop over items len(items) we will reach the end - 1 which last item
# if we start with len(nums) that's mean we start out of boundries index so we need to minus 1, then step back a head one step -1

def traverse_in_reverse_order(lst):
    for i in range(len(lst) -1, 0, -1):
        print(lst[i])
        
        



if __name__ == "__main__":
   traverse_in_reverse_order([1,2,3,4,5,5,6,7,8])