#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#


# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        numA = numL = 0
        for c in s:
            if c == 'A':
                if numA == 1:
                    return False
                numA += 1
            if c == 'L':
                if numL == 2:
                    return False
                numL += 1
            else:
                numL = 0
        return True


# @lc code=end
