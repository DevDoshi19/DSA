def heapify_down(ar,i):
    n = len(ar)

    largest_index = i

    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index <n and ar[left_index] > ar[largest_index]:
        largest_index = left_index
       
    elif right_index <n and  ar[largest_index] < ar[right_index]:
        largest_index = right_index
    
    if largest_index != i :
        ar[i],ar[largest_index] = ar[largest_index],ar[i]
        heapify_down(ar,largest_index)

def heapifyup(ar,i):
    parent_index = (i-1)//2

    if i > 0 and ar[i] > ar[parent_index]:
        ar[i],ar[parent_index] = ar[parent_index],ar[i]
        heapifyup(ar,parent_index)

def min_heap_heapify_down(ar,i):
    n = len(ar)

    small_index = i

    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and ar[left_index] < ar[small_index]:
        small_index = left_index
       
    elif right_index < n and  ar[small_index] > ar[right_index]:
        small_index = right_index
    
    if small_index != i :
        ar[i],ar[small_index] = ar[small_index],ar[i]
        min_heap_heapify_down(ar,small_index)

def min_heap_heapify_up(ar,i):
    parent_index = (i-1)//2

    if i > 0 and ar[i] < ar[parent_index]:
        ar[i],ar[parent_index] = ar[parent_index],ar[i]
        min_heap_heapify_up(ar,parent_index)

def heapfiy(arr,n,i):
    if arr[i] > n :
        arr[i] = n
        heapify_down(arr,i)
    else :
        arr[i] = n
        heapifyup(arr,i)
def min_heapfiy(arr,n,i):
    if arr[i] < n :
        arr[i] = n
        min_heap_heapify_down(arr,i)
    else :
        arr[i] = n
        min_heap_heapify_up(arr,i)

arr= [10,7,6,4,5,4,5,3,2]
n = 1
index = 0
heapfiy(arr,n,index)
print(arr)

min_arr = [1,2,3,4,5,6,7,8,9]
n2 = 10
ind = 0
min_heapfiy(min_arr,n2,ind)
print(min_arr)