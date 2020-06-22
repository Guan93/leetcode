class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = sorted([time[0], time[1], time[3], time[4]])
        res = [c for c in time]

        res[4] = self.nextDigit(res[4], '9', digits)
        if res[4] > time[4]:
            return ''.join(res)

        res[3] = self.nextDigit(res[3], '5', digits)
        if res[3] > time[3]:
            return ''.join(res)

        upper = '3' if time[0] == '2' else '9'
        res[1] = self.nextDigit(res[1], upper, digits)
        if res[1] > time[1]:
            return ''.join(res)

        res[0] = self.nextDigit(res[0], '2', digits)
        return ''.join(res)

    def nextDigit(self, current, upper, digits):
        for digit in digits:
            if digit > current and digit <= upper:
                return digit

        return digits[0]