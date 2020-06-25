class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        count = row = col = i = 0
        while row < rows:
            word = sentence[i]
            # start from the next line
            if col + len(word) > cols - 1:
                row, col = row + 1, 0
            else:
                col += len(word) + 1
                i = (i + 1) % len(sentence)
                if i == 0:
                    count += 1
        return count


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0
        for row in range(rows):
            start += cols
            if s[start % len(sentence)] == ' ':
                start += 1
            else:
                while start > 0 and s[(start - 1) % len(sentence)] != ' ':
                    start -= 1

        return start // len(sentence)