class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        import collections

        if len(words1) != len(words2):
            return False

        sim_map = collections.defaultdict(set)
        for w1, w2 in pairs:
            sim_map[w1].add(w2)
            sim_map[w2].add(w1)

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w1 not in sim_map[w2]:
                return False

        return True