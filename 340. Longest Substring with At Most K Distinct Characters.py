class Solution:

    def lengthOfLongestSubstringKDistinct(self, s, k):
        longest = 0
        left = 0
        char_dict = defaultdict(int)

        for right in range(len(s)):
            char_dict[s[right]] += 1
            while len(char_dict) > k:
                char_dict[s[left]] -= 1
                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        
        return longest

'''
s = eceba
k = 2
''' 