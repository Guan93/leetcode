#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
# sliding window: O(|S| + |T|) and O(|S| + |T|)
from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        count_t = Counter(t)
        count_window = Counter()
        num_required = len(count_t)
        num_found = 0
        left, right = 0, 0
        ans = (float('inf'), 0, -1)  # ans stores (length of substring, left, right)
        while right < len(s):
            char = s[right]
            count_window[char] += 1
            if count_t[char] == count_window[char]:
                num_found += 1
            while left <= right and num_found == num_required:
                char = s[left]
                if count_window[char] == count_t[char]:
                    if right - left + 1 < ans[0]:
                        ans = (right - left + 1, left, right)
                    num_found -= 1
                count_window[char] -= 1
                left += 1
            right += 1
        return s[ans[1]:ans[2] + 1]


# @lc code=end
