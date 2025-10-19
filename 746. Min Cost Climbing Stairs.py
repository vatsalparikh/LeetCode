class TopDownSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 1)
        return self.minCost(cost, memo, len(cost))

    def minCost(self, cost, memo, index):
        if index == 0 or index == 1:
            return 0
        
        if memo[index] == -1:
            memo[index] = min(self.minCost(cost, memo, index - 1) + cost[index - 1], self.minCost(cost, memo, index - 2) + cost[index - 2])

        return memo[index]

class BottomUpSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        min_cost = float('inf')
        for index in range(2, len(cost) + 1):
            min_cost = min(cost[index - 1] + prev1, cost[index - 2] + prev2)
            prev2, prev1 = prev1, min_cost
        return min_cost
        

        