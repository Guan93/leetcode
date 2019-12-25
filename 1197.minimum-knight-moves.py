# # BFS
# from collections import deque

# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         if x == 0 and y == 0:
#             return 0
#         q = deque()
#         seen = {(0, 0)}
#         q.append((0, 0, 0))
#         moves = [(-1, -2), (-1, 2), (1, -2), (1, 2),
#                  (-2, -1), (-2, 1), (2, -1), (2, 1)]
#         while q:
#             curr_x, curr_y, curr_n = q.popleft()
#             for dx, dy in moves:
#                 new_x, new_y, new_n = curr_x + dx, curr_y + dy, curr_n + 1
#                 if new_x == abs(x) and new_y == abs(y):
#                     return new_n
#                 if (new_x > -2 and new_y > -2 and abs(new_x) + abs(new_y) <= 300
#                         and (new_x, new_y) not in seen):
#                     q.append((new_x, new_y, new_n))
#                     seen.add((new_x, new_y))

#         return -1


# # bfs from both source and destination
# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         def dfs(q, seen):
#             new_q = []
#             moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), 
#                      (-2, -1), (-2, 1), (2, -1), (2, 1)]
#             for curr_x, curr_y in q:
#                 for dx, dy in moves:
#                     new_x, new_y = curr_x + dx, curr_y + dy
#                     if (-3 < new_x < abs(x) + 3 and -3 < new_y < abs(y) + 3
#                             and abs(new_x) + abs(new_y) <= 300
#                             and (new_x, new_y) not in seen):
#                         new_q.append((new_x, new_y))
#                         seen.add((new_x, new_y))
#             return new_q

#         q_src, seen_src, n_src = [(0, 0)], {(0, 0)}, 0
#         q_des, seen_des, n_des = [(abs(x), abs(y))], {(abs(x), abs(y))}, 0
#         while True:
#             if seen_src & seen_des:
#                 return n_src + n_des
#             q_src = dfs(q_src, seen_src)
#             n_src += 1
#             if seen_src & seen_des:
#                 return n_src + n_des
#             q_des = dfs(q_des, seen_des)
#             n_des += 1


# dfs with memo
# imagine we are moving the destination point instead
from functools import lru_cache


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def dfs(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
        return dfs(abs(x), abs(y))
