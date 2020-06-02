#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        from collections import Counter

        counts = Counter(words)
        pq = []
        for word, count in counts.items():
            heapq.heappush(pq, Word(word, count))
            if len(pq) > k:
                heapq.heappop(pq)

        return [W.word for W in reversed(pq)]


class Word:
    def __init__(self, word, count) -> None:
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
# @lc code=end

