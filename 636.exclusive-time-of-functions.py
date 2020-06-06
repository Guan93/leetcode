#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#


# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time = [0] * n
        if not logs:
            return time
        stack = []
        prev_flag, prev_ts = None, -1
        for log in logs:
            curr_id, curr_flag, curr_ts = log.split(':')
            curr_id, curr_ts = int(curr_id), int(curr_ts)
            if curr_flag == 'start':
                if stack:
                    time[stack[-1]] += curr_ts - prev_ts - (0 if prev_flag == 'start' else
                                                            1)
                stack.append(curr_id)
            elif curr_flag == 'end':
                prev_id = stack.pop()
                time[prev_id] += curr_ts - prev_ts
                if prev_flag == 'start':
                    time[prev_id] += 1
            prev_flag, prev_ts = curr_flag, curr_ts

        return time

    # concise
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans



# @lc code=end
