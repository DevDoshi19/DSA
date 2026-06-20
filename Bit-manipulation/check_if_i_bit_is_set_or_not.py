n = 13  # 1101 in binary
i_bit = 0  # We want to check if the 1st bit (0-indexed) is set or not

if n & (1 << i_bit) != 0 :   # we are using bitwise AND operator to check if the i_bit is set or not. We left shift 1 by i_bit positions to create a mask that has only the i_bit set. If the result of the bitwise AND operation is not zero, it means that the i_bit is set in n.
    print(f"{i_bit} bit is set in {n}")
    
else:
    print(f"{i_bit} bit is not set in {n}")
    
    
"""using right shift operator"""    
    
i_bit = 2  # We want to check if the 2nd bit (0-indexed) is set or not
if 1 & (n >> i_bit) != 0 :
    print(f"{i_bit} bit is set in {n}")
else:
    print(f"{i_bit} bit is not set in {n}")
    
    
    
"""Clear the ith bit of n"""
n = 13 
i_bit = 2

n = n & ~(1 << i_bit) 

print(f"After clearing the {i_bit} bit, n becomes {n}") 
    
"""set the ith bit of n"""
n = 9 
i_bit = 2

n = n | (1 << i_bit) 

print(f"After setting the {i_bit} bit, n becomes {n}") 