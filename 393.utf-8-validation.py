#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#


# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        ONE_BYTE = 256
        i = 0
        count = 0
        while i < len(data):
            num = data[i] % ONE_BYTE
            if num >> 7 == 0:
                count = 0
            elif num >> 5 == 0b110:
                count = 1
            elif num >> 4 == 0b1110:
                count = 2
            elif num >> 3 == 0b11110:
                count = 3
            else:
                return False
            if len(data) - i - 1 < count:
                return False
            for j in range(1, count + 1):
                if data[i + j] >> 6 != 0b10:
                    return False
            i += count + 1
        return True


# @lc code=end
