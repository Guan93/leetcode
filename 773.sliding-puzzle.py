#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque

        def get_next_states(state):
            states = []
            idx = state.index('0')
            if idx not in (0, 3):
                states.append(state[:idx - 1] + state[idx] + state[idx - 1] + state[idx + 1:])
            if idx not in (2, 5):
                states.append(state[:idx] + state[idx + 1] + state[idx] + state[idx + 2:])
            if idx < 3:
                states.append(state[:idx] + state[idx + 3] + state[idx + 1: idx + 3] + state[idx] + state[idx + 4:])
            if idx >= 3:
                states.append(state[:idx - 3] + state[idx] + state[idx - 2: idx] + state[idx - 3] + state[idx + 1:])
            return states

        state = ''.join([str(board[i][j]) for i in range(2) for j in range(3)])
        seen = set()
        queue = deque([(state, 0)])

        while queue:
            state, n = queue.popleft()
            if state == "123450":
                return n

            seen.add(state)
            for next_state in get_next_states(state):
                if next_state not in seen:
                    queue.append((next_state, n + 1))

        return -1
# @lc code=end

