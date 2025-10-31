class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = dict()
        return self.recurse(text1, text2, len(text1) - 1, len(text2) - 1, memo)

    def recurse(self, text1, text2, index1, index2, memo):
        if index1 < 0 or index2 < 0:
            return 0

        if (index1, index2) in memo:
            return memo[(index1, index2)]

        if text1[index1] == text2[index2]:
            memo[(index1, index2)] = 1 + self.recurse(text1, text2, index1 - 1, index2 - 1, memo)
            return memo[(index1, index2)]

        memo[(index1, index2)] = max(self.recurse(text1, text2, index1, index2 - 1, memo), self. recurse(text1, text2, index1 - 1, index2, memo))

        return memo[(index1, index2)]