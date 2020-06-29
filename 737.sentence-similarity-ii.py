class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        def dfs(start, target, seen):
            if start not in graph:
                return False
            if start == target:
                return True
            seen.add(start)
            for nei in graph[start]:
                if nei in seen:
                    continue
                if dfs(nei, target, seen):
                    return True
            return False

        if len(words1) != len(words2):
            return False

        graph = dict()
        for w1, w2 in pairs:
            s1 = graph.get(w1, set())
            s1.add(w2)
            graph[w1] = s1

            s2 = graph.get(w2, set())
            s2.add(w1)
            graph[w2] = s2

        for w1, w2 in zip(words1, words2):
            if not dfs(w1, w2, set()):
                return False

        return True

