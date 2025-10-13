class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        max_variance = 0
        for i in range(n):
            for j in range(i,n):
                freq = [0] * 26
                for k in range(i,j+1):
                    freq[ord(s[k]) - ord('a')] += 1

                max_freq = 0
                min_freq = float('inf')

                for count in freq:
                    if count > 0:
                        max_freq = max(max_freq, count)
                        min_freq = min(min_freq, count)
                
                variance = max_freq - min_freq
                max_variance = max(max_variance, variance)
        
        return max_variance