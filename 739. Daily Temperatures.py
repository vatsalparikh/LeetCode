# O(n) time and space
# minor space optimization, not storing temperature in stack, even better
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater = [0] * len(temperatures)
        stack = deque()
        
        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                popped_index = stack.pop()
                next_greater[popped_index] = index - popped_index
            stack.append(index)
        
        return next_greater

'''
next_greater: 1, 1, 4, 2, 1, 1, 0, 0
stack: [76, 6], [73, 0]
'''

# O(n) time and space
# minor optimization: updating next_greater in one pass
class OnePassSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater = [0] * len(temperatures)
        stack = deque()
        
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                popped_temp, popped_index = stack.pop()
                next_greater[popped_index] = index - popped_index
            stack.append([temperature, index])
        
        return next_greater

'''
next_greater: 1, 1, 4, 2, 1, 1, 0, 0
stack: [76, 6], [73, 0]
'''

# O(n) time and space
class OriginalSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_greater = [-1] * len(temperatures)
        stack = deque()
        
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                popped_temp, popped_index = stack.pop()
                next_greater[popped_index] = index
            stack.append([temperature, index])
        
        for index in range(len(next_greater)):
            if next_greater[index] == -1:
                next_greater[index] = 0
            else:
                next_greater[index] -= index
        
        return next_greater

'''
next_greater: 1, 1, 4, 2, 1, 1, 0, 0
stack: [76, 6], [73, 0]
'''