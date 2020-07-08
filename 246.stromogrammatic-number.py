class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        for i in range(len(num) // 2):
            if num[i] not in pairs or pairs[num[i]] != num[-(i + 1)]:
                return False
        return True