import collections


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                           website: List[str]) -> List[str]:
        user_visits = collections.defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visits[u].append((t, w))

        counts = collections.Counter()
        for user in user_visits:
            websites = [w for _, w in sorted(user_visits[user])]
            print(user, self.get_Nsequence(3, websites))
            for s in self.get_Nsequence(3, websites):
                counts[s] += 1

        max_visits = 0
        max_seq = tuple()
        for s, c in counts.items():
            if c > max_visits:
                max_seq = s
                max_visits = c
            elif c == max_visits:
                max_seq = min(max_seq, s)

        return max_seq

    def get_Nsequence(self, n, websites):
        if n == 1:
            return [(w, ) for w in set(websites)]
        res = []
        seen = set()
        for i in range(len(websites) - n + 1):
            first = websites[i]
            if first in seen:
                continue
            seen.add(first)
            res.extend(
                [(first, *seq) for seq in self.get_Nsequence(n - 1, websites[i + 1:])])
        return res