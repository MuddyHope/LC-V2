"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # stack?
        stack = []
        intervals.sort(key=lambda interval: interval.start)
        for interval in intervals:
            _start, _end = interval.start, interval.end
            if stack and stack[-1] > (_start):
                return False
            else:
                stack.append(_end)
        return True