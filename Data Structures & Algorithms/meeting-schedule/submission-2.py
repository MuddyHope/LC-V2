"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:
            return True
        
        intervals = sorted(intervals, key= lambda x: x.start)
    
        _start = intervals[0].start
        _endtime = intervals[0].end

        for meeting in intervals[1:]:
            print(f"endtime: {_endtime}, starttime: {meeting.start}")
            if meeting.start < _endtime:
                return False
            _endtime = meeting.end
        return True



            