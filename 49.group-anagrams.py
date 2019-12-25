#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

import collections
from typing import List


# @lc code=start
class Solution:
    # hashtable key as sorted string
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = collections.defaultdict(list)
    #     for s in strs:
    #         res[tuple(sorted(s))].append(s)
    #     return list(res.values())

    # hashtable key as count
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


# @lc code=end
