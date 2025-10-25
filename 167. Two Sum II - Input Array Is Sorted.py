class TwoPointerSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return [1,2]

class BinarySearchSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            low = index + 1
            high = len(numbers) - 1
            temp_target = target - numbers[index]
            print('index, temp_target', index, temp_target)
            while low <= high:
                mid = low + ((high - low) // 2)
                print('index, mid', index, mid)
                if numbers[mid] == temp_target:
                    return [index + 1, mid + 1]
                elif numbers[mid] < temp_target:
                    low = mid + 1
                else:
                    high = mid - 1
        return [1, 2]



'''

-1, -3, -5, target = -2
'''