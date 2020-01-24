#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

# @lc code=start
class Solution:
    # def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dfs(i, curr_width, curr_height):
    #         if i == len(books):
    #             return curr_height

    #         book_width, book_height = books[i]

    #         min_height = curr_height + dfs(i + 1, book_width, book_height)
    #         if book_width + curr_width <= shelf_width:
    #             min_height = min(min_height, dfs(i + 1, book_width + curr_width, max(curr_height, book_height)))

    #         return min_height

    #     return dfs(0, 0, 0)

    # # dfs: O(num_books * shelf_width) and O(num_books * shelf_width)
    # def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
    #     """
    #     The curr_height parameter does not need to be memorized. For each book i,
    #     and for each curr_width, we can only store the minimum height for the remaining
    #     books [i...n].
    #     """
    #     from collections import defaultdict

    #     def dfs(i, curr_width, curr_height, memo):
    #         if i == len(books):
    #             return curr_height

    #         if curr_width in memo[i]:
    #             return memo[i][curr_width]

    #         book_width, book_height = books[i]

    #         min_height = curr_height + dfs(i + 1, book_width, book_height, memo)
    #         if book_width + curr_width <= shelf_width:
    #             min_height = min(min_height, dfs(i + 1, book_width + curr_width, max(curr_height, book_height), memo))
    #         memo[i][curr_width] = min_height
    #         return min_height

    #     memo = defaultdict(dict)
    #     return dfs(0, 0, 0, memo)

    # dp: O(n^2) and O(n). dp[i] means the minimum height for books[0...i-1]
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]

# @lc code=end

