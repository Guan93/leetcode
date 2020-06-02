#
# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#

# @lc code=start
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict

        duplicates = defaultdict(list)

        for path in paths:
            blocks = path.split(' ')
            directory, files_with_content = blocks[0], blocks[1:]
            for f in files_with_content:
                idx = f.index('(')
                file_name, file_content = f[:idx], f[idx + 1: -1]
                duplicates[file_content].append(f"{directory}/{file_name}")

        return [val for key, val in duplicates.items() if len(val) > 1]


"""
    Q: Imagine you are given a real file system, how will you search files? DFS or BFS?
    A: In a real file system, the number of files in folders is usually larger than the
       depths of folders, so bfs is likely to consume more memory. On the other hand,
       given disc operation is very very slow, bfs will potentially be faster than dfs,
       as it might make better use of spatial locality.

    Q: If the file content is very large (GB level), how will you modify your solution?
    A: Files with different sizes are guaranteed to be different. We can hash a small part
       of the files with equal sizes (using MD5 for example). Only if the md5 is same will
       we compare the file byte to byte.

    Q: If you can only read the file by 1kb each time, how will you modify your solution?
    A:

    Q: What is the time complexity of your modified solution? What is the most
    A:

    Q: time-consuming part and memory consuming part of it? How to optimize?
    A:

    Q: How to make sure the duplicated files you find are not false positive?
    A:
"""
# @lc code=end

