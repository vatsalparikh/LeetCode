'''
3Sum is somewhere between medium and hard
Brute force for 3Sum is O(n^3) and optimal solution is O(n^2)
Two Sum Input is Sorted should be solved first. This solves two sum in O(n) time complexity
This helps in solving 3Sum in O(n^2)

Some things to keep in mind:
i, j, k are indices and they should be distinct in 3Sum
continue logic and incrementing left, right is necessary to avoid duplicate triplets
here duplicate means [1,0,-1], [1,0,-1]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                addition = nums[index] + nums[left] + nums[right]
                if addition == 0:
                    triplets.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif addition > 0:
                    right -= 1
                else:
                    left += 1
        return triplets