# Unlike sum, where adding more numbers only increases/decreases monotonically, product flips sign with negatives.
# A very negative product might become the maximum if multiplied by another negative.
# Zero resets everything (product becomes 0).
# 👉 You can’t just track the "max so far" — you also need to track the min so far, because it might turn into a large positive later.
# This is the critical leap from max-sum (Kadane’s) to max-product.

# At each position, the maximum product ending here can only come from: 
# The current number itself, or
# Current number × previous max, or
# Current number × previous min (if both are negative)

Time: O(n) Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = maximum = nums[0]
        for index in range(1, len(nums)):
            temp_max = curr_max
            curr_max = max(curr_max * nums[index], curr_min * nums[index], nums[index])
            curr_min = min(temp_max * nums[index], curr_min * nums[index], nums[index])
            maximum = max(maximum, curr_max)
        return maximum

