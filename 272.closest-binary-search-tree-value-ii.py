# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# inorder dfs: O(n) and O(n)
class Solution1:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        from collections import deque

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)

        inorder = []
        dfs(root)
        lo, hi = 0, len(inorder)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if inorder[mid] <= target:
                lo = mid + 1
            else:
                hi = mid

        left, right = lo - 1, lo
        res = deque()
        while len(res) < k:
            if left < 0:
                res.append(inorder[right])
                right += 1
            elif right >= len(inorder):
                res.appendleft(inorder[left])
                left -= 1
            else:
                if target - inorder[left] < inorder[right] - target:
                    res.appendleft(inorder[left])
                    left -= 1
                else:
                    res.append(inorder[right])
                    right += 1
        return res


class Solution2:
    # two stacks: O(h + k) and O(n)
    # building each stack took O(h);
    # cost for get_prev / get_next is amortized to O(1) since each node is pushed
    # and popped at most once
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # reverse inorder traverse the tree for one step
        def get_prev(stack):
            if not stack:
                return
            node = stack.pop()
            curr = node.left
            while curr:
                stack.append(curr)
                curr = curr.right
            return node.val

        # inorder traverse the tree for one step
        def get_next(stack):
            if not stack:
                return
            node = stack.pop()
            curr = node.right
            while curr:
                stack.append(curr)
                curr = curr.left
            return node.val

        prev_stack, next_stack = [], []
        res = []

        # init two stacks
        curr = root
        while curr:
            if curr.val < target:
                prev_stack.append(curr)
                curr = curr.right
            else:
                next_stack.append(curr)
                curr = curr.left

        prev, next_ = get_prev(prev_stack), get_next(next_stack)
        while k > 0:
            if not prev:
                res.append(next_)
                next_ = get_next(next_stack)
            elif not next_:
                res.append(prev)
                prev = get_prev(prev_stack)
            else:
                if target - prev < next_ - target:
                    res.append(prev)
                    prev = get_prev(prev_stack)
                else:
                    res.append(next_)
                    next_ = get_next(next_stack)
            k -= 1

        return res