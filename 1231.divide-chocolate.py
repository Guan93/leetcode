class Solution:
    def maximizeSweetness(self, A, K):
        left, right = 1, int(sum(A) / (K + 1)) + 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = cuts = 0
            for a in A:
                if cur + a <= mid:
                    cur += a
                else:
                    cuts += 1
                    cur = 0
            if cuts > K:
                left = mid + 1
            else:
                right = mid - 1
        return left
