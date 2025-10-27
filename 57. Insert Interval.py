class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for index in range(len(intervals)):
            if newInterval[1] < intervals[index][0]:
                result.append(newInterval)
                result += intervals[index:]
                return result
            elif newInterval[0] > intervals[index][1]:
                result.append(intervals[index])
            else:
                newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        result.append(newInterval)
        return result