#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        def update_chars(prev_count, prev, chars):
            nonlocal ptr
            chars[ptr] = prev
            ptr += 1
            if prev_count > 1:
                for i in str(prev_count):
                    chars[ptr] = i
                    ptr += 1

        ptr = 0
        prev = None
        prev_count = 0
        for c in chars:
            if c == prev:
                prev_count += 1
            else:
                if prev_count > 0:
                    update_chars(prev_count, prev, chars)
                prev, prev_count = c, 1

        update_chars(prev_count, prev, chars)

        for _ in range(len(chars) - ptr):
            chars.pop()

        return ptr

# @lc code=end

