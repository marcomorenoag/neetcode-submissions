"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        '''
        time   0  .  10  .  20  .  30
        int[0] #  #  #   #  #   #  #
        int[1] .  #  #   .  .   .  .
        int[2] .  .  .   #  #   .  .

        [30, 10, 20
        '''

        # Base cases
        if not intervals or len(intervals) == 0:
            return 0
        
        # Build min heap
        free_rooms = []

        # Sort meetings by start time in increasing order
        intervals.sort(key=lambda x: x.start)

        heapq.heappush(free_rooms, intervals[0].end)

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)

        return len(free_rooms)

            
