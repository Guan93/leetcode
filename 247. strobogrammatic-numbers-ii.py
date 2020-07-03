class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        single = ['0', '1', '8']
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        if n == 0:
            return []

        if n % 2 == 0:
            res = ['']
        else:
            res = [i for i in single]

        for i in range(n // 2 - 1):
            old_res = res
            res = []
            for key, value in pairs.items():
                for num in old_res:
                    res.append(key + num + value)

        if n // 2 >= 1:
            old_res = res
            res = []
            for i in ['1', '6', '8', '9']:
                for num in old_res:
                    res.append(i + num + pairs[i])

        return res