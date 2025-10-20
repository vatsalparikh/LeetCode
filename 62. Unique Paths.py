# O(mn) time and O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[n-1]

# O(mn) time and space
class MemoSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        row, col = m, n
        memo = [[0 for _ in range(col)] for _ in range(row)]
        return self.unique(row - 1, col - 1, memo)

    def unique(self, row, col, memo):
        if row <= 0 or col <= 0:
            return 1

        if memo[row][col] == 0:
            memo[row][col] = self.unique(row - 1, col, memo) + self.unique(row, col - 1, memo)
        
        return memo[row][col]

# O(2^(m+n)) time and O(m+n) space
class ExponentialSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m - 1, n - 1
        # memo = [[0 for _ in range(cols)] for _ in range(rows)]
        return self.unique(rows, cols)

    def unique(self, rows, cols):
        if rows <= 0 or cols <= 0:
            return 1

        return self.unique(rows - 1, cols) + self.unique(rows, cols - 1)