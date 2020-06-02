#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def bt(i, num, prev, curr):
            if num == 4:
                return
            if i == len(s):
                if num == 3:
                    res.append(f"{prev}.{curr}")
                return

            new_prev = f"{prev}.{curr}" if len(prev) > 0 else str(curr)
            bt(i + 1, num + 1, new_prev, int(s[i]))
            new_curr = curr * 10 + int(s[i])
            if curr > 0 and new_curr < 256:
                bt(i + 1, num, prev, new_curr)

        res = []
        if len(s) > 0:
            bt(1, 0, "", int(s[0]))
        return res


# @lc code=end
