#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#


# @lc code=start
from collections import Counter


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        curr_votes = Counter()
        lead_votes = lead_person = -1
        self.lead_persons = []
        for p, t in zip(persons, times):
            curr_votes[p] += 1
            if curr_votes[p] >= lead_votes:
                lead_votes, lead_person = curr_votes[p], p
            self.lead_persons.append((t, lead_person))

    def q(self, t: int) -> int:
        lo, hi = 0, len(self.lead_persons)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.lead_persons[mid][0] <= t:
                lo = mid + 1
            else:
                hi = mid
        return self.lead_persons[lo - 1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end
