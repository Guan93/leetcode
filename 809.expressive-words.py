#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
import collections


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def _helper(s):
            char, counts = "", []
            prev, count = s[0], 0
            for i in range(len(s)):
                if s[i] == prev:
                    count += 1
                else:
                    char += prev
                    counts.append(count)
                    prev = s[i]
                    count = 1
            char += prev
            counts.append(count)
            return char, counts
        
        R, count = _helper(S)
        ans = 0
        for word in words:
            R2, count2 = _helper(word)
            if R2 != R: continue
            ans += all(c1 == c2 or c1 >= max(c2, 3) for c1, c2 in zip(count, count2))
        return ans
