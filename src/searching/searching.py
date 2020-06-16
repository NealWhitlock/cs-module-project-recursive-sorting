# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case - arr has len 0 or 1 return that arr
    if len(arr) < 1:
        return -1
    if start == end:
        return start

    middle_index = (start+end)//2
    # get 'middle' index and check if that's the value
    if arr[middle_index] == target:
        return middle_index
        # if 'middle' is less than the value, update the start to be middle + 1
    elif arr[middle_index] < target:
        start = (start+end)//2 + 1
    # else, update the end to be middle - 1
    else:
        end = (start+end)//2 - 1
    
    return binary_search(arr, target, start, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

