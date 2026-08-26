from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # If the earliest available room is free
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # Assign this meeting to a room
            heapq.heappush(rooms, end)

        return len(rooms)