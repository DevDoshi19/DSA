class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        prev = [0 for _ in range(target + 1)] 

        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= target:
                prev[arr[0]] = 1

        for index in range(1, n):
            curr = [0 for _ in range(target + 1)]
            for total in range(target + 1):
                not_pick = prev[total]
                pick = 0
                if arr[index] <= total:
                    pick = prev[total - arr[index]]
                curr[total] = pick + not_pick
            prev = curr
    
        return prev[target]   