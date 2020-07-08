#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#


# @lc code=start
# O(nlogn + len(S))
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str],
                          targets: List[str]) -> str:
        if not indexes:
            return S
        indexes, sources, targets = list(zip(*sorted(zip(indexes, sources, targets))))
        indexes.append(len(S))
        res = S[:indexes[0]]
        for i in range(len(indexes) - 1):
            start, end = indexes[i], indexes[i + 1]
            mid = start + len(sources[i])
            if S[start:mid] == sources[i]:
                res += targets[i] + S[mid:end]
            else:
                res += S[start:end]
        return res


# @lc code=end
