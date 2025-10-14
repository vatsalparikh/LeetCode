class BruteForceSolution:
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


class OptimizedSolution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        max_variance = 0

        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        
        for i in range(26):
            for j in range(26):
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue

                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                major_count = 0
                minor_count = 0
                remaining_minor = counter[j]

                for ch in s:
                    if ch == major:
                        major_count += 1
                    if ch == minor:
                        minor_count += 1
                        remaining_minor -= 1

                    if minor_count > 0:
                        max_variance = max(max_variance, major_count - minor_count)

                    if major_count < minor_count and remaining_minor > 0:
                        major_count = 0
                        minor_count = 0

        return max_variance
