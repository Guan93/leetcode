#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        num_ones = []
        for i in range(num + 1):
            count = 0
            mask = 1
            for k in range(32):
                if mask & i:
                    count += 1
                mask = mask << 1
            num_ones.append(count)
        return num_ones

    # dp + most significant bit
    def countBits(self, num: int) -> List[int]:
        num_ones = [0] * (num + 1)
        i, b = 0, 1
        while b <= num:
            while i < b and i + b <= num:
                num_ones[i + b] = num_ones[i] + 1
                i += 1
            i = 0
            b = b << 1
        return num_ones

    # dp + least significant bit
    # def countBits(self, num: int) -> List[int]:
    #     num_ones = []
    #     for i in range(num + 1):
    #         count = 0
    #         if i == 0 or i == 1:
    #             count = i
    #         else:
    #             count = num_ones[i >> 1] + (i & 1)
    #         num_ones.append(count)
    #     return num_ones


# @lc code=end
