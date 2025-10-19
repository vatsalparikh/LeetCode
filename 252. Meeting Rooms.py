"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        for index in range(len(sorted_intervals) - 1):
            curr_interval = sorted_intervals[index]
            next_interval = sorted_intervals[index + 1]
            if curr_interval.end > next_interval.start:
                return False
        return True