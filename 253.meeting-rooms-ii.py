#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start


# O(n^2) and O(1)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        num_rooms = 0
        while intervals:
            start = intervals.pop(0)
            num_rooms += 1
            i = 0
            while intervals and i < len(intervals):
                if intervals[i][0] >= start[1]:
                    start = intervals.pop(i)
                else:
                    i += 1
        return num_rooms


# heap: O(nlogn) and O(n)
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for meeting in intervals[1:]:
            if free_rooms[0] <= meeting[0]:
                free_rooms.pop()
            heapq.heappush(free_rooms, meeting[1])

        return len(free_rooms)


# chronological ordering: maintaining two separate sorted array for start time
# and end time: O(logn) and O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])

        num_rooms = 0
        L = len(intervals)
        start_ptr = end_ptr = 0
        while start_ptr < L:
            if start_timings[start_ptr] < end_timings[end_ptr]:
                num_rooms += 1
            else:
                end_ptr += 1
            start_ptr += 1
        
        return num_rooms


# @lc code=end
