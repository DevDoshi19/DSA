def isMinHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] < arr[i]:
            return False
        if right_child < n and arr[right_child] < arr[i]:
            return False
    return True
    
def isMaxHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[i]:
            return False
        if right_child < n and arr[right_child] > arr[i]:
            return False
    return True

arr = [4,6,9,12,16,13,19,21]
print("Check whether the array is MinHeap for element : [4,6,9,12,16,13,19,21] ",isMinHeap(arr))
print("Check whether the array is MaxHeap for element : [4,6,9,12,16,13,19,21] ",isMaxHeap(arr))

arr1 = [10,9,8,7,6,5,4,3,2]
print("Check whether the array is MinHeap for element : [10,9,8,7,6,5,4,3,2] ",isMinHeap(arr1))
print("Check whether the array is MaxHeap for element : [10,9,8,7,6,5,4,3,2] ",isMaxHeap(arr1))
