# Insertion Sort is a simple and intuitive sorting algorithm 
# that works by building a sorted portion of the array one element at a time. 
# It repeatedly picks the next element and inserts it into the correct position within the sorted portion of the array.

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
        
        arr[j+1] = key
        print(arr)

given_arr = [12, 11, 13, 5, 6]
print (given_arr)
insertion_sort(given_arr)
print(given_arr)



# Second way

# def insertion_sort(data: list[int]) -> list[int]:
#     for i, current in enumerate(data):
#         j = i - 1
#         while j >= 0 and data[j] > current:
#             data[j+1] = data[j]
#             j -= 1
#         data[j+1] = current
#     return data

# print(insertion_sort([5, 4, 9, 7, 3, 6]))