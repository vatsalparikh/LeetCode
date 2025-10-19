class TopDownSolution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        return self.climb(n, memo)

    def climb(self, n, memo):
        if n == 0 or n == 1:
            return 1

        if memo[n-2] == 0:
            memo[n-2] = self.climb(n-2, memo)

        if memo[n-1] == 0:
            memo[n-1] = self.climb(n-1, memo)

        return memo[n-2] + memo[n-1]