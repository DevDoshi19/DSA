class Solution:
    # t.c = O(n) and s.c = O(k) where k is the number of symbols in the roman numeral representation of the number

    def intToRoman(self, num: int) -> str:
        values = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C", 
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }

        ans = []
        i = 0
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while num >0 :
            while num > 0 and  num >= nums[i] :
                num = num - nums[i]
                ans.append(values[nums[i]])
            
            i += 1 

        return "".join(ans)
    
"""
• Optimal Time Complexity: It runs in O(1) constant time. Because the input num is strictly capped at 3999 for Roman numerals, the loop will execute at most a fixed number of times regardless of how large the input is.
• Optimal Space Complexity: It uses O(1) constant auxiliary space, as the size of the lookup table/arrays is fixed.
• Greedy Strategy: Explain that you are always taking the largest possible Roman numeral chunk out of the number first.
"""

class Solution2:

  def intToRoman(self, num: int) -> str:
    # Combined lookup table prevents indexing mismatches
    mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    ans = []

    for value, symbol in mapping:
      if num == 0:
        break
      # divmod gives you both the multiplier and the remainder
      count, num = divmod(num, value)
      ans.append(symbol * count)

    return "".join(ans)
