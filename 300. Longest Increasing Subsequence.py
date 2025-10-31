# Best solution: O(n^2) time and O(n) space
class DPSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for curr in range(1, len(nums)):
            for prev in range(curr):
                if nums[curr] > nums[prev]:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)

class MemoizedSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = dict()
        if not nums:
            return 0
        else:
            return max(self.lis(nums, i, memo) for i in range(len(nums)))

    def lis(self, nums, start, memo):
        if start == len(nums):
            return 0
        
        if start in memo:
            return memo[start]

        longest = 1
        for index in range(start + 1, len(nums)):
            if nums[index] > nums[start]:
                longest = max(longest, 1 + self.lis(nums, index, memo))

        memo[start] = longest
        return memo[start]