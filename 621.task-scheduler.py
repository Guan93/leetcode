#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_count = num_max = 0
        counter = [0] * 26
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
            max_count = max(max_count, counter[ord(task) - ord('A')])
        for c in counter:
            num_max += c == max_count

        num_intervals = max_count - 1
        idles_in_one_interval = max(0, n - num_max + 1)
        total_idles_available = idles_in_one_interval * num_intervals
        tasks_left = len(tasks) - max_count * num_max
        idles_left = max(0, total_idles_available - tasks_left)
        res = idles_left + len(tasks)

        return res


# @lc code=end
