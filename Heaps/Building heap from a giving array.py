def heapifydown(arr,i):
    n = len(arr)
    largest = i 

    left_index = 2*i + 1
    right_index = 2*i + 2
    if left_index < n and arr[left_index] > arr[largest] :
        largest = left_index
    if right_index < n and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != i :
        arr[i],arr[largest] = arr[largest],arr[i]
        heapifydown(arr,largest)
    return arr

def max_heap(arr,i):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapifydown(arr,i)       
    return arr

arr = [1,8,7,16,11,12,2,4]
print(max_heap(arr,0))


# max heap 
# |_ heapifydown : That means we are checking the parent node with its child node and if the child node is greater than the parent node then we will swap the parent node with the child node and then we will call the heapifydown function again for the child node.
# |_ heapifyup : That means we are checking the child node with its parent node and if the child node is greater than the parent node then we will swap the child node with the parent node and then we will call the heapifyup function again for the parent node.

# min heap
# |_ min_heap_heapify_down : That means we are checking the parent node with its child node and if the child node is smaller than the parent node then we will swap the parent node with the child node and then we will call the min_heap_heapify_down function again for the child node.
# |_ min_heap_heapify_up : That means we are checking the child node with its parent node and if the child node is smaller than the parent node then we will swap the child node with the parent node and then we will call the min_heap_heapify_up function again for the parent node.