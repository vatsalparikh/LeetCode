# here I only compare if s2 <= e1
# that's sufficient because the list is sorted and so s1 will always be <= e2, so this check can be skipped
# also sorting list in place avoids the need for extra space
class EfficientSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]
        for index in range(1, len(intervals)):
            first = merged[-1]
            second = intervals[index]
            if second[0] <= first[1]:
                merged[-1][1] = max(first[1], second[1])
            else:
                merged.append(second)
        return merged

# I am doing full demorgan check, but because the list is already sorted it's unnecessary
class RedundantChecksSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        merged = [sorted_intervals[0]]
        for index in range(1, len(sorted_intervals)):
            first = merged[-1]
            second = sorted_intervals[index]
            if first[0] <= second[1] and second[0] <= first[1]:
                merged[-1] = [first[0], max(first[1], second[1])]
            else:
                merged.append(second)
        return merged