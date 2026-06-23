def heapify_down(arr, i):
    n = len(arr)

    largest_index = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[largest_index]:
        largest_index = left_index
    
    if right_index < n and arr[right_index] > arr[largest_index]:
        largest_index = right_index

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify_down(arr, largest_index)

    return arr

def min_heap_to_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, i)

    return arr

arr = [2,4,7,6,10,9,11,9]
print("Min Heap : ", arr)
print("Max Heap : ", min_heap_to_max_heap(arr))