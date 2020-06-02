#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    # O(nlogn + m) and O(n + m)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []
        for log in logs:
            space_idx = log.index(' ')
            if log[space_idx + 1].isalpha():
                letter_logs.append((log, space_idx))
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x[0][x[1] + 1:len(x[0])], x[0][:x[1]]))
        return [log for log, _ in letter_logs] + digit_logs

    # concise one
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)

# @lc code=end

