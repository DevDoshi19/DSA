def hepifydown(arr,n,i):

    largest_index = i

    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index <n and arr[left_index] < arr[largest_index]:
        largest_index = left_index
       
    if right_index <n and  arr[largest_index] > arr[right_index]:
        largest_index = right_index
    
    if largest_index != i :
        arr[i],arr[largest_index] = arr[largest_index],arr[i]
        hepifydown(arr,n,largest_index)

def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n//2-1,-1,-1):
        hepifydown(arr,n,i)

    # extract element form the heap one by one 
    for last_index in range(n-1,0,-1):
        arr[0] ,arr[last_index]=arr[last_index],arr[0]
        hepifydown(arr,last_index,0)

    return arr

arr = [1,4,7,6,10,9,11,9]
print(heap_sort(arr))
