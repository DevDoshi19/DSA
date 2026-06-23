class MaxHeap:

    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent] < self.arr[i]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                break

    def heapifydown(self, arr, i):
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
            self.heapifydown(arr, largest_index)  # ✅ fixed

    def pop(self):
        if not self.arr:
            return None
        n = len(self.arr)
        self.arr[0], self.arr[n-1] = self.arr[n-1], self.arr[0]  # ✅ fixed
        val = self.arr.pop()
        new_n = len(self.arr)
        for i in range(new_n//2 - 1, -1, -1):  # ✅ fixed
            self.heapifydown(self.arr, i)
        return val