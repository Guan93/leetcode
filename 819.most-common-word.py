#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#


# @lc code=start
class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re

        banned = set(banned)
        count = dict()
        mf_count, mf_word = 0, ""
        for word in re.split(" |\!|\?|'|,|;|\.", paragraph):
            if len(word) == 0:
                continue
            word = word.lower()
            if word in banned:
                continue
            count[word] = count.get(word, 0) + 1
            if count[word] > mf_count:
                mf_count, mf_word = count[word], word

        return mf_word


class Solution2:
    def mostCommonWord(self, paragraph, banned):
        import collections

        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans


# @lc code=end
