# Bubble Sort is a simple comparison-based sorting algorithm. 
# It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# This process is repeated until the list is sorted.

# Algorithm Steps:
# Compare the first two elements. If the first is greater than the second, swap them.
# Move to the next pair and repeat the comparison and swapping.
# Continue until the end of the list is reached.
# Repeat the entire process, reducing the number of elements to compare in each pass, as the largest element is already in place.
# Stop when no swaps are made during a pass (the list is sorted).

# Explanation:
# The outer loop runs for every element in the array.
# The inner loop compares adjacent elements and swaps them if they are in the wrong order.
# The swapped flag helps in optimizing the algorithm by stopping early if the list is already sorted before completing all iterations.

def BubbleSort (arr : list[int]) -> list[int]:
    arr_len = len(arr)
    for i in range(arr_len):
        swapped = False
        for j in range (arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
            print(f"loop {j}", end=" ")
        print(arr)
        if not swapped:
            break
    return arr

input_array = [1,2,3,9,11,6,7,8]
print(f"Given Array: {input_array}")
sorted_array = BubbleSort(input_array)
print(f"Sorted Array: {sorted_array}")