import operator


# binary search: O((len(word)) * logn) and O(1)
class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        lo, hi = 0, len(products)
        i = 0
        res = []
        for i in range(len(searchWord)):
            new_lo = self.bisect(products, i, searchWord[i], lo, hi, 'left')
            new_hi = self.bisect(products, i, searchWord[i], lo, hi, 'right')
            res.append(products[new_lo:min(new_lo + 3, new_hi)])
            lo, hi = new_lo, new_hi
        return res

    def bisect(self, l, i, target, lo, hi, direction='left'):
        """
        i: search for the ith character in a word
        """
        assert direction in ('left', 'right'), 'parameter direction must be either "left" or "right"'
        op = operator.lt if direction == 'left' else operator.le
        while lo < hi:
            mid = lo + (hi - lo) // 2
            c = l[mid][i] if i < len(l[mid]) else chr(0)
            if op(c, target):
                lo = mid + 1
            else:
                hi = mid
        return lo



# another binary search: one search per iteration
class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        import bisect

        products.sort()
        cur, ans = '', []
        for char in searchWord:
            cur += char
            i = bisect.bisect_left(products, cur)
            ans.append([product for product in products[i : i + 3] if product.startswith(cur)])
        return ans