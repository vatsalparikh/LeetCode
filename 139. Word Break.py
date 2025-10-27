# Time: O(n^3) Space: O(n + m) where n is memo and m is wordset
# Time complexity considers O(n) subproblems * O(n) for loop * O(m) slicing. Interesting!
class MemoizedSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = dict()
        return self.canBreak(s, wordset, 0, memo)

    def canBreak(self, s, wordset, start, memo):
        if start in memo:
            return memo[start]

        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordset and self.canBreak(s, wordset, end, memo):
                memo[start] = True
                return True
            
        memo[start] = False
        return False

# Time: O(2^(n-1)) Space: O(n) for recursion depth and O(m) for wordset
class RecursiveSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [False] * len(s)
        return self.canBreak(s, wordset, 0, dp)

    def canBreak(self, s, wordset, start):
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordset and self.canBreak(s, wordset, end):
                dp[]
                return True
            
        return False