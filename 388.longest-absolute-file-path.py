#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#


# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def construct_tree():
            nonlocal i
            level = count_level(path[i])
            root = Node(path[i][level:])
            i += 1
            while i < len(path):
                nxt_level = count_level(path[i])
                if level == nxt_level:
                    break
                child = construct_tree()
                root.children.append(child)
            return root

        def count_level(name):
            count = 0
            for s in name:
                if s == '\t':
                    count += 1
                else:
                    break
            return count

        def dfs(node):
            if not node:
                return 0
            if not node.children:
                return len(node.val) if '.' in node.val else -float('inf')
            return len(node.val) + max([dfs(child) for child in node.children]) + 1

        path = input.split('\n')
        i = 0
        root = construct_tree()
        return dfs(root)


# precise: https://leetcode.com/problems/longest-absolute-file-path/discuss/86615/9-lines-4ms-Java-solution
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        stack = [0]
        for s in input.split('\n'):
            num_tabs = s.count('\t')
            level = num_tabs + 1

            while len(stack) > level:
                stack.pop()
            cur_len = stack[-1] + len(s) - num_tabs + 1
            stack.append(cur_len)
            if '.' in s:
                max_len = max(max_len, cur_len - 1)

        return max_len


# @lc code=end
