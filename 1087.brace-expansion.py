class Solution:
    def expand(self, S: str) -> List[str]:
        res = [""]
        in_braces = False
        for c in S:
            if c == ',':
                continue
            if c == '{':
                options = ""
                in_braces = True
            elif c == '}':
                options = sorted(options)
                tmp = []
                for i in range(len(res)):
                    for c in options:
                        tmp.append(res[i] + c)
                res = tmp
                in_braces = False
            elif in_braces:
                options += c
            else:
                for i in range(len(res)):
                    res[i] += c
        return res
