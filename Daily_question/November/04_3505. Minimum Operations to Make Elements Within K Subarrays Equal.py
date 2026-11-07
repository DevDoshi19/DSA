from sortedcontainers import SortedSet # pyright: ignore[reportMissingImports]
from ast import List
from bisect import bisect_left

# brute force approach
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        window = [0] * (n-x+1)

        for i in range(n-x+1):
            new_arr = sorted(nums[i:i+x])
            median = new_arr[x//2]

            window[i] = sum(
                abs(num-median) for num in new_arr
            )

        INF = float("inf")

        dp = [[INF] * (k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, k+1):

                dp[i][j] = dp[i-1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i-x][j-1] + window[i-x]
                    )

        return dp[n][k]


class Solution2:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        left = SortedSet()
        right = SortedSet()

        sum_left = 0
        sum_right = 0

        target = (x + 1) // 2

        def rebalance():
            nonlocal sum_left, sum_right

            while len(left) > target:
                item = left.pop()
                right.add(item)

                sum_left -= item[0]
                sum_right += item[0]

            while len(left) < target and right:
                item = right.pop(0)
                left.add(item)

                sum_right -= item[0]
                sum_left += item[0]

        def add(num, idx):
            nonlocal sum_left, sum_right

            item = (num, idx)

            if not left or item <= left[-1]:
                left.add(item)
                sum_left += num
            else:
                right.add(item)
                sum_right += num

            rebalance()

        def remove(num, idx):
            nonlocal sum_left, sum_right

            item = (num, idx)

            if item in left:
                left.remove(item)
                sum_left -= num
            else:
                right.remove(item)
                sum_right -= num

            rebalance()

        def get_cost():
            median = left[-1][0]

            return (
                median * len(left) - sum_left
                + sum_right - median * len(right)
            )

        for i in range(x):
            add(nums[i], i)

        window = []

        for i in range(n - x + 1):

            window.append(get_cost())

            if i < n - x:
                remove(nums[i], i)
                add(nums[i + x], i + x)

        INF = float("inf")

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + window[i - x]
                    )

        return dp[n][k]

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        total = 0

        while i > 0:
            total += self.tree[i]
            i -= i & -i

        return total

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit

            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]

            bit >>= 1

        return idx + 1


class Solution3:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        values = sorted(set(nums))
        m = len(values)

        def get_index(num):
            return bisect_left(values, num) + 1

        count_bit = Fenwick(m)
        sum_bit = Fenwick(m)

        def update(num, delta):
            idx = get_index(num)

            count_bit.add(idx, delta)
            sum_bit.add(idx, num * delta)

        for num in nums[:x]:
            update(num, 1)

        window = []

        total_sum = sum(nums[:x])

        for i in range(n - x + 1):

            median_idx = count_bit.kth((x + 1) // 2)
            median = values[median_idx - 1]

            left_count = count_bit.query(median_idx)
            left_sum = sum_bit.query(median_idx)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            window.append(cost)

            if i < n - x:
                outgoing = nums[i]
                incoming = nums[i + x]

                update(outgoing, -1)
                update(incoming, 1)

                total_sum += incoming - outgoing

        INF = float("inf")

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                dp[i][j] = dp[i - 1][j]

                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + window[i - x]
                    )

        return dp[n][k]
