class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for index in range(len(s)):
            odd = self.expand(s, index, index)
            even = self.expand(s, index, index+1)
            if len(longest) < len(odd):
                longest = odd
            if len(longest) < len(even):
                longest = even
        return longest

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]