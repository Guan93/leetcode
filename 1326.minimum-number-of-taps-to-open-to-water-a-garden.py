# essentially the same as #1024.video-stitching
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = sorted([(i - r, i + r) for i, r in enumerate(ranges)])

        max_reach = num_taps = i = 0
        while max_reach < n:
            curr_max_reach = 0
            while i < n + 1 and intervals[i][0] <= max_reach:
                curr_max_reach = max(curr_max_reach, intervals[i][1])
                i += 1
            if curr_max_reach <= max_reach:
                return -1
            max_reach, num_taps = curr_max_reach, num_taps + 1

        return num_taps
