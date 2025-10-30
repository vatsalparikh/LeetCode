# O(1) space
class SpaceOptimizedSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        from_right = 1

        for index in range(1, len(nums)):
            result[index] = result[index-1] * nums[index-1]
        
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= from_right
            from_right *= nums[index]

        return result

# O(n) time and O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [1] * len(nums)
        from_right = [1] * len(nums)
        result = []

        for index in range(1, len(nums)):
            from_left[index] = from_left[index-1] * nums[index-1]
        print(from_left)
        
        for index in range(len(nums) - 2, -1, -1):
            from_right[index] = from_right[index+1] * nums[index+1]
        print(from_right)

        for index in range(len(nums)):
            result.append(from_left[index] * from_right[index])

        return result

'''
 0  1 2 3
 1  1 2 6
24 12 4 1

 0  1  2  3  4
 1 -1 -1  0  0
 0  0 -9  3  1
[0 0 9 0 0]
'''
        