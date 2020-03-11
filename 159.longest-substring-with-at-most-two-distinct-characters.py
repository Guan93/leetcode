class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import Counter

        count = Counter()
        num_distinct = 0
        lo = hi = 0
        max_len = 0

        while hi < len(s):
            count[s[hi]] += 1
            if count[s[hi]] == 1:
                num_distinct += 1

            while num_distinct > 2:
                if count[s[lo]] == 1:
                    num_distinct -= 1
                count[s[lo]] = count[s[lo]] - 1
                lo = lo + 1

            max_len = max(max_len, hi - lo + 1)
            hi += 1

        return max_len