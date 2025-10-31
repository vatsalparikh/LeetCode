class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

'''
3,4,5,1,2

mid val = 5
5 > 3
5 > 2 go right
so left = index 3
'''