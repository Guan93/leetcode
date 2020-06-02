class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        def float2str(f, n_digits=3):
            i, dec = str(round(f, n_digits)).split('.')
            dec += '0' * (n_digits - len(dec))
            return f"{i}.{dec}"

        num_zeros = s = 0
        resids = [.0] * len(prices)
        for i in range(len(prices)):
            int_, dec = prices[i].split('.')
            resids[i] = int(dec) / 1000
            s += int(int_)
            if resids[i] == 0:
                num_zeros += 1
        exceeds = target - s

        if not 0 <= exceeds <= len(prices) - num_zeros:
            return "-1"

        resids.sort(reverse=True)
        res = 0
        for i in range(exceeds):
            res += 1 - resids[i]
        for i in range(exceeds, len(resids)):
            res += resids[i]
        return float2str(res)
