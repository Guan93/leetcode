class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = dict()

    def add_next(self, node):
        if node.val not in self.next:
            self.next[node.val] = node


class DFS:
    def __init__(self, graph) -> None:
        self.has_cycle = False
        self._seen = set()
        self._on_stack = set()
        self.post = list()

        for letter, node in graph.items():
            if letter not in self._seen:
                self._dfs(node)

    def get_topological(self):
        return "".join(reversed(self.post)) if not self.has_cycle else ""

    def _dfs(self, node):
        self._seen.add(node.val)
        self._on_stack.add(node.val)

        for nei in node.next:
            if self.has_cycle:
                return
            if nei not in self._seen:
                self._dfs(node.next[nei])
            elif nei in self._on_stack:
                self.has_cycle = True
                return

        self._on_stack.discard(node.val)
        self.post.append(node.val)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = dict()
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = Node(letter)

        for prev, nxt in zip(words, words[1:]):
            letter_pairs = list(zip(prev, nxt))
            for i, pair in enumerate(letter_pairs):
                if (pair[0] != pair[1]
                        and (i == 0 or letter_pairs[i - 1][0] == letter_pairs[i - 1][1])):
                    graph[pair[0]].add_next(graph[pair[1]])

        dfs = DFS(graph)
        return dfs.get_topological()
