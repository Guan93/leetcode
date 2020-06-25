from collections import defaultdict


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.dictionary = defaultdict(set)
        for word in dictionary:
            abbr = self.get_abbr(word)
            self.dictionary[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self.get_abbr(word)
        if (abbr not in self.dictionary
                or len(self.dictionary[abbr]) == 1 and word in self.dictionary[abbr]):
            return True
        else:
            return False

    def get_abbr(self, word):
        return word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)