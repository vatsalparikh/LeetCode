class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        rows = len(matrix)
        cols = len(matrix[0])
        high = (rows * cols) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


'''
mid = low + ((high - low) // 2)
row = mid // n;
col = mid % n;
cols or n = 4
mid = 4, 5, 6, 7 should map to row 1 how?
4 // 4 = 1
4 % 4 = 0
5 // 4 = 1
5 % 4 = 1
'''