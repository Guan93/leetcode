class _Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = dict()
        self.rank = 0
        self.is_end = False


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self._root = _Node()
        self.keyword = ""
        for sentence, time in zip(sentences, times):
            self.put(sentence, time)

    def put(self, sentence, time):
        p = self._root
        for c in sentence:
            if c not in p.next:
                p.next[c] = _Node()
            p = p.next[c]
        p.val = sentence
        p.rank -= time
        p.is_end = True

    def _dfs(self, root, res):
        if root.is_end:
            res.append((root.rank, root.val))
        for c in root.next:
            self._dfs(root.next[c], res)

    def start_with(self, prefix):
        res = []
        p = self._root
        for c in prefix:
            if c not in p.next:
                return res
            p = p.next[c]
        self._dfs(p, res)
        return res

    def input(self, c: str):
        if c == '#':
            self.put(self.keyword, 1)
            self.keyword = ""
            return []
        self.keyword += c
        return [item[1] for item in sorted(self.start_with(self.keyword))][:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)