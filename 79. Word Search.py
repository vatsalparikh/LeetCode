'''
Time: O(mn * 4^l) Space: O(l)
where m is num of rows and n is num of cols and l is word length
the branching factor is 4, depth is the number of characters in the word, which is l
and this happens once for every character in the cell m * n times, so time complexity is m * n * 4^l
here we are using board to keep track of visiting nodes, so space complexity is O(l)
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, word, row, col, 0):
                    return True
        return False

    def backtrack(self, board, word, row, col, index):
        if index == len(word):
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] == '#' or board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = self.backtrack(board, word, row-1, col, index+1) or \
                self.backtrack(board, word, row+1, col, index+1) or \
                self.backtrack(board, word, row, col-1, index+1) or \
                self.backtrack(board, word, row, col+1, index+1)

        board[row][col] = temp
        return found

'''
Time: O(mn * 4^l) Space: O(mn + l)
where m is num of rows and n is num of cols and l is word length
the branching factor is 4, depth is the number of characters in the word, which is l
and this happens once for every character in the cell m * n times, so time complexity is m * n * 4^l
here we are using visiting to keep track of visiting nodes, so space complexity is O(mn + l)
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visiting = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, word, row, col, visiting, 0):
                    return True
        return False

    def backtrack(self, board, word, row, col, visiting, index):
        if index == len(word):
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or visiting[row][col] == True or board[row][col] != word[index]:
            return False

        visiting[row][col] = True

        found = self.backtrack(board, word, row-1, col, visiting, index+1) or \
                self.backtrack(board, word, row+1, col, visiting, index+1) or \
                self.backtrack(board, word, row, col-1, visiting, index+1) or \
                self.backtrack(board, word, row, col+1, visiting, index+1)

        visiting [row][col] = False
        return found