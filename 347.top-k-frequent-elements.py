#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    # heap: O(nlogk) and O(k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        pq = []
        counter = Counter(nums)
        for num in counter:
            heapq.heappush(pq, (counter[num], num))
            if len(pq) > k:
                heapq.heappop(pq)

        return [num for _, num in pq]

    # quicksort O(n)

    # bucket: O(n) and O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            max_freq = max(counter[num], max_freq)

        bucket = [list() for _ in range(max_freq)]
        for num in counter:
            bucket[counter[num] - 1].append(num)

        res = []
        for freq in reversed(range(len(bucket))):
            for num in bucket[freq]:
                if len(res) == k:
                    return res
                res.append(num)
        return res

# @lc code=end
