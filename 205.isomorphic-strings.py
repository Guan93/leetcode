#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
# # O(n) and O(??)
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         s_to_t = dict()
#         t_to_s = dict()
#         for i in range(len(s)):
#             if s[i] not in s_to_t and t[i] not in t_to_s:
#                 s_to_t[s[i]] = t[i]
#                 t_to_s[t[i]] = s[i]
#             if s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]:
#                 return False
#         return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = [0] * 256, [0] * 256
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = d2[ord(t[i])] = i + 1
        return True
# @lc code=end
