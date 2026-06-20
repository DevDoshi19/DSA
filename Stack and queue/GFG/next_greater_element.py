def next_greater_element(nums):
    stack = []
    n = len(nums)
    ans = [-1] * n 

    for i in range(n-1,-1,-1):
        while stack and stack[-1] < nums[i]:
            stack.pop()
        if stack :
            ans[i] = stack[-1]
        stack.append(nums[i])

    return ans

result = next_greater_element([19,2,4,9,3,5,8,10])
print(result)