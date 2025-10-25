class Solution:

    def longestSameCharSubstring(s):
        char_set = set()
        longest = 0
        left = 0
        while right < len(s):
            if s[index] not in char_set:
                right += 1
                left = right
            else:
                right += 1
                longest = max(longest, right - left + 1)
        return longest