class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.recurse(nums, 0, memo)

    def recurse(self, nums, index, memo):
        if index >= len(nums):
            return 0
        
        if memo[index] != -1:
            return memo[index]

        memo[index] = max(nums[index] + self.recurse(nums, index + 2, memo), self.recurse(nums, index + 1, memo))

        return memo[index]