'''
Meeting rooms II is about max number of overlapping intervals
Non-overlapping intervals is about max number of non-overlapping intervals
'''


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)
        start = 0
        end = 0
        rooms = 0
        max_rooms = 0
        while start < len(starts) and end < len(ends):
            if starts[start] < ends[end]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start += 1
            else:
                rooms -= 1
                end += 1
        return max_rooms
        