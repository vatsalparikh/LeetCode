class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        char_dict = defaultdict(int)
        left = 0

        for right in range(len(s)):
            char_dict[s[right]] += 1
            max_freq = max(char_dict.values())
            while right - left + 1 - max_freq > k:
                char_dict[s[left]] -= 1
                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1
            longest = max(longest, right - left + 1)

        return longest