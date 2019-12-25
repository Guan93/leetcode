# m is the length of source and n is the length of target
# # O(mn) and O(1)
# class Solution:
#     def shortestWay(self, source: str, target: str) -> int:
#         chars_available = [False] * 26
#         for char in source:
#             chars_available[ord(char) - ord('a')] = True
#         # maintain two pointers here: i for target and j for source
#         i, j, res = 0, 0, 1
#         while i < len(target):
#             if not chars_available[ord(target[i]) - ord('a')]:
#                 return -1
#             # find a char in source so that source[j] == target[i]
#             while j < len(source) and target[i] != source[j]:
#                 j += 1
#             if j == len(source):
#                 res += 1
#                 j = -1
#                 i -= 1
#             i, j = i + 1, j + 1
#         return res


# # O(nlogm) and O(m)

# import bisect


# class Solution:
#     """
#     Instead of itering through source every time, we can use binary search.
#     """

#     def shortestWay(self, source: str, target: str) -> int:
#         idx = [[] for _ in range(26)]
#         for i, c in enumerate(source):
#             idx[ord(c) - ord('a')].append(i)
#         i, j, res = 0, 0, 1
#         while i < len(target):
#             target_idx = idx[ord(target[i]) - ord('a')]
#             if not target_idx:
#                 return -1
#             # find a char in source so that source[j] == target[i]
#             k = bisect.bisect_left(target_idx, j)
#             if k >= len(target_idx):
#                 res += 1
#                 j = 0
#             else:
#                 j = target_idx[k] + 1
#                 i += 1
#         return res


# linear time O(26 * M + N)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idx = [[0] * len(source) for _ in range(26)]
        for i in range(len(source)):
            idx[ord(source[i]) - ord('a')][i] = i + 1
        for i in range(26):
            pre = 0
            for j in reversed(range(len(source))):
                if idx[i][j] == 0:
                    idx[i][j] = pre
                else:
                    pre = idx[i][j]

        i, j, res = 0, 0, 1
        while i < len(target):
            if j == len(source):
                j = 0
                res += 1
            if idx[ord(target[i]) - ord('a')][0] == 0:
                return -1
            j = idx[ord(target[i]) - ord('a')][j]
            if j == 0:
                res += 1
            i += 1
        return res
