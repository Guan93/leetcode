#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def count_match(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    count += 1
            return count

        num_matches = 0
        while num_matches < 6:
            min_idx, min_count = 0, float("inf")
            for i in range(len(wordlist)):
                count = sum([
                    count_match(wordlist[i], wordlist[j]) == 0
                    for j in range(len(wordlist))
                ])
                if count < min_count:
                    min_count, min_idx = count, i

            num_matches = master.guess(wordlist[min_idx])
            wordlist = [
                word for word in wordlist
                if count_match(word, wordlist[min_idx]) == num_matches
            ]


# @lc code=end
