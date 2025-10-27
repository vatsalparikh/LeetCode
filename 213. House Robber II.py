class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        

        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)
        memo1[len(nums) - 1] = 0
        memo2[0] = 0
        return max(self.recurse(nums, 0, len(nums) - 1, memo1), self.recurse(nums, 1, len(nums), memo2))

    def recurse(self, nums, start, end, memo):
        if start >= end:
            return 0

        if memo[start] != -1:
            return memo[start]

        memo[start] = max(nums[start] + self.recurse(nums, start + 2, end, memo), self.recurse(nums, start + 1, end, memo))

        return memo[start]