class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.backtrack(nums, 0, [], subsets)
        return subsets

    def backtrack(self, nums, start, subset, subsets):
        subsets.append(subset.copy())

        for index in range(start, len(nums)):
            subset.append(nums[index])
            self.backtrack(nums, index + 1, subset, subsets)
            subset.pop()