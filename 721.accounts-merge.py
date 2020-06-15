#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#


# @lc code=start
# graph: O(nlogn) and O(n)

class Node:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.nei = set()


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(email, res):
            seen.add(email)
            res.append(email)
            for nei in graph[email].nei:
                if nei in seen:
                    continue
                dfs(nei, res)

        graph = dict()
        # build graph
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in graph:
                    graph[email] = Node(name, email)
                for nei in account[1:]:
                    if nei not in graph:
                        graph[nei] = Node(name, nei)
                    if nei != email:
                        graph[email].nei.add(nei)

        res = []
        seen = set()
        for email in graph:
            if email in seen:
                continue
            emails = []
            dfs(email, emails)
            res.append([graph[email].name] + sorted(emails))
        return res


# @lc code=end
