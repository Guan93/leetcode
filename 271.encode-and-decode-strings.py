# chunked transfer: O(n) and O(n)
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('/')
            res.append(s)
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """

        res = []
        prev = 0
        while True:
            try:
                curr = s.index('/', prev)
            except ValueError:
                return res
            length = int(s[prev:curr])
            prev = curr + 1 + length
            res.append(s[curr + 1:prev])


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
