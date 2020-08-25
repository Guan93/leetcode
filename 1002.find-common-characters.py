#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
import collections


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        prev_counts = collections.Counter(A[0])
        for word in A[1:]:
            new_counts = collections.Counter(word)
            for c in new_counts.keys():
                if c not in prev_counts:
                    new_counts[c] = 0
                else:
                    new_counts[c] = min(prev_counts[c], new_counts[c])
            prev_counts = new_counts

        res = []
        for c in prev_counts:
            if prev_counts[c] == 0:
                continue
            res.extend([c] * prev_counts[c])

        return res


# @lc code=end
