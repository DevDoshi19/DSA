class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        new_s=1
        while self.stack and self.stack[-1][0] <= price :
            p,s = self.stack.pop()
            new_s += s 

        self.stack.append([price,new_s])
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
LeetCode #901: Online Stock Span
Don't search for the pattern yet.
Example:
prices = [100, 80, 60, 70, 60, 75, 85]

output = [1, 1, 1, 2, 1, 4, 6]

For each price, return the number of consecutive days up to today where the price was less than or equal to today's price.
For 75:
60, 70, 60, 75
 ↑              ↑
4 consecutive days

First question only:
If today's price is 75, what information from the previous days do we actually need to calculate its span?
"""