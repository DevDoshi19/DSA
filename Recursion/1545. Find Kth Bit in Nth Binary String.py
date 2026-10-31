"""
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.


intiution:
Okay so the institution was same as the prev. one, but there is slight change like we are additional of 2 things,
1) add "1" 
2) rev(inverse(str)) and we need to pass the output in str 

so the basic idea was same , we will use recursion and go till edge case. 
there are mainly 2 edge case 1 is if we found k = 1 and n =1 that means we reach end so return "0" and 2nd is if we found k value is == mid , that means we are getting "1" , so don't need to go backward form here .

intuition behind the left part is same , check for the n-1 row and call recursively, but for right part, 

1) we can see that we have rev. of the invert string, so for what index we get in right we need to do 1 - ans , that solve the problem of reverse , but finding a right index is real problem. 

2) so let's understand the basic idea and my idea behind this.... if the 
total length is = l 
the index for right half is = k 
so the distance is = k - mid 
it reverse so , for left side we need to find the index for k value. 
for left the mid distance is =  s ... which is the mid - right_half 

now example : 
k = 14 , n =4 
so the right_half index is 14 - 8 = 6 means the k distance is 6 away from mid , so we need mid - right_half to find same distance from mid , so it's 8 -6 which is 2. that give us the right index to find value 

the t.c. = O(n) , because we are decrese 1 value at time of n and s.c. = O(n), stack space. 

"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 and k == 1 :
            return "0"
        
        length = pow(2,n) - 1
        mid = ( length //2 ) + 1 
        
        if k == mid :
            return "1"
        elif k < mid :
            return self.findKthBit(n-1,k)
        else:
            right_half = k - mid
            index = mid-right_half
            return str(1 - int(self.findKthBit(n-1,index)))

# brute force approach is to find the string and return the value at k-1 index, but that will take O(2^n) time and space.
class Solution2:
    def findKthBit(self,n:int,k:int)->str:
        s = "0"
        for i in range(2,n+1):
            s = s + "1" + "".join(["1" if x == "0" else "0" for x in s[::-1]])

        return s[k-1]