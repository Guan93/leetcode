#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import Counter

        res = Counter()
        for s in cpdomains:
            count, domain = s.split(' ')
            count = int(count)
            subs = domain.split('.')
            for i in reversed(range(len(subs))):
                domain = '.'.join(subs[i:])
                res[domain] += count

        return [f"{count} {domain}" for domain, count in res.items()]

# @lc code=end

