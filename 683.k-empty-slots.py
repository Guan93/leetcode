class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        def helper(i):
            left_flag = right_flag = True
            for dist in range(1, K + 1):
                left, right = i - dist, i + dist
                if left_flag:
                    if left < 0 or bulb_array[left] == 1:
                        left_flag = False
                if right_flag:
                    if right >= n or bulb_array[right] == 1:
                        right_flag = False
            return ((left_flag and i - (K + 1) >= 0 and bulb_array[i - (K + 1)] == 1)
                    or (right_flag and i + (K + 1) < n and bulb_array[i + (K + 1)] == 1))

        n = len(bulbs)
        bulb_array = [0] * n
        for i, x in enumerate(bulbs):
            bulb_array[x - 1] = 1
            if helper(x - 1):
                return i + 1
        return -1
