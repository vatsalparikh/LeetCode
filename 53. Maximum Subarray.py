class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = running_sum = nums[0]
        for index in range(1, len(nums)):
            running_sum = max(running_sum + nums[index], nums[index])
            max_sum = max(max_sum, running_sum)
        return max_sum