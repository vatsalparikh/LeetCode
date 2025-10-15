class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            char_set = set()
            length = 0
            for j in range(i, n):
                if s[j] not in char_set:
                    char_set.add(s[j])
                    length += 1
                else:
                    break
            longest = max(longest, len(char_set))
        return longest

class OptimizedSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        longest = 0
        left = 0

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(longest, right - left + 1)

        return longest