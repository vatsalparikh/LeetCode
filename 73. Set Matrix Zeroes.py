class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # save first row and first col information about zeroes, if any
        first_row_zero = any(matrix[0][col] == 0 for col in range(cols))
        first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

        # store 0s in the first row / first col for other rows
        for row_index in range(1, rows):
            for col_index in range(1, cols):
                if matrix[row_index][col_index] == 0:
                    matrix[row_index][0] = 0
                    matrix[0][col_index] = 0
        
        # mark 0s for rows and cols starting from index 1
        # this also marks 0s for rows and cols starting from 1
        # for originally existing 0s for first row and col
        for row_index in range(1, rows):
            for col_index in range(1, cols):
                if matrix[row_index][0] == 0 or matrix[0][col_index] == 0:
                    matrix[row_index][col_index] = 0

        # mark first row or first col zero if any original zeroes existed before processing
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0


'''
0,1,2,0
3,4,5,0
1,3,1,0

1,0,1
0,0,0
1,0,1
'''
        