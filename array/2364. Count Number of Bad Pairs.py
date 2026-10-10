class Solution:
    
    # count the number of good pairs in the array
    # t.c. = O(n), S.c. = O(n) 

    def countBadPairs(self, nums: list[int]) -> int:
        mp = {}
        n = len(nums)
        total_pairs = (n*(n-1)//2)
        good_pairs = 0

        for key,value in enumerate(nums):
            val = value - key
            good_pairs += mp.get(val,0)
            mp[val] = mp.get(val,0) + 1 

        return total_pairs-good_pairs

# step 1 : first we check the total number of pairs in the array using the formula n*(n-1)/2
# step 2 : we count goof pairs using the formula nums[i] - i = nums[j] - j, we can use a hashmap to store the frequency of each value of nums[i] - i and for each value we can add the frequency of that value to the good_pairs count.