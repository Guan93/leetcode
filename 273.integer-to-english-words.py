#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        def less_hundred(num):
            if num < 10:
                return one(num)
            if num < 20:
                return two_less_20(num)

            tens, rem = divmod(num, 10)
            res = ten(tens)
            if rem:
                res += f" {one(rem)}"
            return res

        def less_thousand(num):
            hundred, rem = divmod(num, 100)
            res = []
            if hundred:
                res.append(f"{one(hundred)} Hundred")
            if rem:
                res.append(less_hundred(rem))
            return ' '.join(res)

        if not num:
            return "Zero"

        units = ["Thousand", "Million", "Billion"]
        level = -1
        res = []
        quo, rem = divmod(num, 1000)
        if rem:
            res.append(less_thousand(rem))

        while quo:
            level += 1
            quo, rem = divmod(quo, 1000)
            if rem:
                res.append(f"{less_thousand(rem)} {units[level]}")

        return ' '.join(res[::-1])

# @lc code=end

