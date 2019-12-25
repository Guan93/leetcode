#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        while True:
            length_inline = 0
            words_inline = []
            while i < len(words) and length_inline + len(words[i]) + len(words_inline) <= maxWidth:
                words_inline.append(words[i])
                length_inline += len(words[i])
                i += 1
            if i == len(words):
                res.append(' '.join([word for word in words_inline]) + ' ' * (maxWidth - length_inline - len(words_inline) + 1))
                break
            if len(words_inline) == 1:
                res.append(words_inline[0] + ' ' * (maxWidth - length_inline))
            else:
                line_string = ""
                space_between, space_left = divmod(maxWidth - length_inline, len(words_inline) - 1)
                for j in range(len(words_inline) - 1):
                    line_string += words_inline[j] + ' ' * space_between
                    if space_left > 0:
                        line_string += ' '
                        space_left -= 1
                line_string += words_inline[-1]
                res.append(line_string)
        return res

# @lc code=end
