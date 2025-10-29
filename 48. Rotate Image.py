class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # transpose the matrix over the main diagonal
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # reverse each row in the matrix (left to right)
        # here row reversal means reversing all elements within a row, not reversing rows themselves
        for row in range(len(matrix[0])):
            matrix[row].reverse()