Space: O(1), Time: O(mn)
class SpaceOptimizedSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    self.traverse(grid, row, col)
                    num_islands += 1
        return num_islands

    def traverse(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'

        self.traverse(grid, row-1, col)
        self.traverse(grid, row+1, col)
        self.traverse(grid, row, col-1)
        self.traverse(grid, row, col+1)


Time: O(mn) Sapce: O(mn)
m is the number of rows and n is the number of columns
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not visited[row][col]:
                    self.traverse(grid, row, col, visited)
                    num_islands += 1
        return num_islands

    def traverse(self, grid, row, col, visited):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col] == True or grid[row][col] == '0':
            return
        
        visited[row][col] = True

        self.traverse(grid, row-1, col, visited)
        self.traverse(grid, row+1, col, visited)
        self.traverse(grid, row, col-1, visited)
        self.traverse(grid, row, col+1, visited)