#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans = []
        k = 0
        for s in reversed(S):
            if s == '-':
                continue
            s = s.upper()
            if k == K:
                ans.append('-')
                k = 0
            k += 1
            ans.append(s)
        return ''.join(ans[::-1])

# @lc code=end
