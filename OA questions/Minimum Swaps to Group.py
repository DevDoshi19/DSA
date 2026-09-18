"""
We have only 0 and 1, and we want all 0s on one side and all 1s on the other side, using the minimum number of adjacent swaps.

The solution considers both possible final arrangements:

000...111
or
111...000

Then it counts how many swaps each arrangement requires and takes the minimum.
"""

def minMoves(arr):
    zero_seen = 0 
    one_seen = 0 
    # 000...111 
    swaps_0_left = 0 
    # 111...000 
    swaps_1_left = 0 

    for x in arr:
        if x == 0:
            swaps_1_left += one_seen 
            zero_seen += 1
        else: 
            swaps_0_left += zero_seen 
            one_seen += 1
        
        print(f"element : {x}, one_seen: {one_seen}, zero_seen: {zero_seen}, swaps_0_left: {swaps_0_left}, swaps_1_left: {swaps_1_left}")
                
    return min(swaps_0_left, swaps_1_left)

arr = [1,0,0,1,0,1,0,0,1]
arr2 = [1,1,1,1,0,0,0,0]
print(minMoves(arr))
print(minMoves(arr2))