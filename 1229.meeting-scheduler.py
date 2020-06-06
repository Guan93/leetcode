class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            (s1, e1), (s2, e2) = slots1[p1], slots2[p2]
            if s1 < e2 and s2 < e1:
                e, s = min(e1, e2), max(s1, s2)
                if e - s >= duration:
                    return [s, s + duration]
            if e1 > e2:
                p2 += 1
            else:
                p1 += 1
        return []