#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # # extra space, three (can be two) iterations
    # def isPalindrome(self, s: str) -> bool:
    #     s_list = []
    #     for c in s.lower():
    #         if ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
    #             s_list.append(c)
    #     mid = len(s_list) // 2
    #     p1, p2 = (mid, mid) if len(s_list) % 2 == 1 else (mid - 1, mid)

    #     while p1 >= 0:
    #         if s_list[p1] != s_list[p2]:
    #             return False
    #         p1, p2 = p1 - 1, p2 + 1

    #     return True

    # one iteration: O(n) and O(1)
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 <= p2:
            c1, c2 = s[p1].lower(), s[p2].lower()
            if not c1.isalnum():
                p1 += 1
            elif not c2.isalnum():
                p2 -= 1
            elif c1 == c2:
                p1, p2 = p1 + 1, p2 - 1
            else:
                return False

        return True

# @lc code=end

