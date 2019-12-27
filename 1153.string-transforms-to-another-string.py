class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True

        trans_map = dict()
        for c1, c2 in zip(str1, str2):
            if trans_map.setdefault(c1, c2) != c2:
                return False

        return len(set(str2)) < 26
