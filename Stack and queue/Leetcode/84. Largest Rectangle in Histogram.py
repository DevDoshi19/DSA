class Solution:

    """
    Pattern recognition:
    Observation                   -   Action
    Current height is larger      -   Push it
    Current height is equal       -   Can merge/update starting position
    Current height is smaller     -   Pop taller bars and calculate areas
    End of array                  -   Process remaining bars

    1.What am I maximizing? Height × width.
    2.What limits a rectangle? A smaller bar on either side.
    3.When do I discover the right limit? When a smaller bar arrives.
    4.Can I process bars only once? Yes, using a monotonic stack.
    5.What is the time complexity? O(n).
    6.What is the space complexity? O(n).
    7.What must I remember? Height and the earliest index it can extend from.
    
    """

    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h :
                index,height = stack.pop()
                width = i-index
                max_area = max(max_area,height*width)
                start = index

            stack.append((start,h)) 
            
            
        n = len(heights)
        while stack :
            index,height = stack.pop()
            width = n - index
            max_area = max(max_area, height * width)

        return max_area