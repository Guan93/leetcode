#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#

# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        max_reach = i = 0
        num_clips = 0
        while max_reach < T:
            curr_max_reach = 0
            while i < len(clips) and clips[i][0] <= max_reach:
                curr_max_reach = max(curr_max_reach, clips[i][1])
                i += 1
            if curr_max_reach <= max_reach:
                return -1
            max_reach, num_clips = curr_max_reach, num_clips + 1

        return num_clips


# @lc code=end

