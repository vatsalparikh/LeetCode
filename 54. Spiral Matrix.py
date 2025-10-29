class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        spiral = []

        while left <= right and top <= bottom:

            # move from left to right
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

            # move from top to bottom
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # move from right to left
                for col in range(right, left - 1, - 1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # move from bottom to top
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral