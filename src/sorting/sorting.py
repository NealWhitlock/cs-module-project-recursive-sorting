# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    index = 0

    # Compare first element in each list.

    while arrA and arrB:  # While elements are in both aarA and aarB
        if arrA[0] < arrB[0]:  # if the first element in aarA is less
            merged_arr[index] = (arrA.pop(0))  # pop it from aarA and put in merged_aar
        else:
            merged_arr[index] = (arrB.pop(0))  # pop first element of aarB to put in merged_aar
        index += 1

    if not arrA:  # If aarA is empty
      for j in range(index, len(merged_arr)):  # Loop through aarB and add to merged_aar
        merged_arr[j] = (arrB.pop(0))
    else:  # If aarB is empty
      for j in range(index, len(merged_arr)):  # Loop through aarA and add to merged_aar
        merged_arr[j] = (arrA.pop(0))


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    # Split arr in half and repeat until each element is in it's own list
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

