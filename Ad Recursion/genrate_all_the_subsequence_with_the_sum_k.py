nums = [1,2,3]
k = 3

result = []
def solve(index,subset):
    if index >= len(nums):
        if sum(subset) == k:
            result.append(subset.copy())
        return 
            
    subset.append(nums[index])
    solve(index+1,subset)
    subset.pop()
    solve(index+1,subset)

    
solve(0,[])
print(result)