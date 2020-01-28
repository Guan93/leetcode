#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = 1 if numerator * denominator >= 0 else -1
        rem, divisor = abs(numerator), abs(denominator)
        quo, rem = divmod(rem, divisor)
        res = str(quo) if sign > 0 else f"-{quo}"
        if rem > 0:
            dec_part = []
            seen = dict()
            idx = 0

            while rem > 0 and rem not in seen:
                seen[rem] = idx
                idx += 1
                quo, rem = divmod(rem * 10, divisor)
                dec_part.append(str(quo))
            dec_part = "".join(dec_part)
            if rem > 0:
                dec_part = f'{dec_part[:seen[rem]]}({dec_part[seen[rem]:]})'

            res += '.' + dec_part
        return res


# @lc code=end

