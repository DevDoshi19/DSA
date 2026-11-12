class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # cost = 0
        # if (cost1+cost2)<=costBoth:
        #     return (cost1*need1) + (cost2*need2)
        # else:
        #     mini = min(need1,need2)
        #     total = costBoth*mini
        #     return total + ((need1-mini)*min(cost1,costBoth) if need1-mini != 0 else (need2-mini)*min(cost2,costBoth))

        mini_cost = min(cost1+cost2,costBoth)
        min_need = min(need1,need2)
        total = min_need * mini_cost
        cost_rem = ((need1-min_need) * min(cost1,costBoth)) + ((need2-min_need) * min(cost2,costBoth))

        return cost_rem + total