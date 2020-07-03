class Solution1:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        import bisect

        f = lambda x: a * x**2 + b * x + c

        if a == 0:
            return [f(x) for x in (nums if b > 0 else nums[::-1])]

        center = -b / 2 / a
        hi = bisect.bisect_left(nums, center)
        lo = hi - 1

        res = []
        while len(res) < len(nums):
            if lo >= 0 and hi < len(nums):
                if center - nums[lo] < nums[hi] - center:
                    res.append(f(nums[lo]))
                    lo -= 1
                else:
                    res.append(f(nums[hi]))
                    hi += 1
            elif lo >= 0:
                res.append(f(nums[lo]))
                lo -= 1
            else:
                res.append(f(nums[hi]))
                hi += 1

        return res if a > 0 else res[::-1]


# https://leetcode.com/problems/sort-transformed-array/discuss/83331/Python-O(n)-Two-Pointers-Solution
class Solution2:
    def sortTransformedArray(self, nums, a, b, c):
        nums = [x*x*a + x*b + c for x in nums]
        ret = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                ret[i] = nums[p1]
                p1 += 1
            else:
                ret[i] = nums[p2]
                p2 -=1
            i += d
        return ret