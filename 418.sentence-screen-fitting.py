# brute force: LTE
class Solution1:
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


# fit one row at a time
class Solution2:
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


# build a map first
# O(n * (cols // avg_word_len)) + O(rows), O(n) where n = len(sentence)
class Solution3:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # when current line starts with word sentence[i],
        # next_idx[i]: next line will start with word sentence[next_idx[i]]
        # times[i]: the number of times the sentence will be repeated in this line
        next_idx = [0] * len(sentence)
        times = [0] * len(sentence)

        for i in range(len(sentence)):
            cur, cur_len, time = i, 0, 0
            while cur_len + len(sentence[cur]) <= cols:
                cur_len += len(sentence[cur]) + 1
                cur += 1
                if cur == len(sentence):
                    cur = 0
                    time += 1
            next_idx[i] = cur
            times[i] = time

        res = 0
        cur = 0
        for row in range(rows):
            res += times[cur]
            cur = next_idx[cur]

        return res

