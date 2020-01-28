#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = []
    #     for i in range(1, n + 1):
    #         if not i % 3 and not i % 5:
    #             res.append("FizzBuzz")
    #         elif not i % 3:
    #             res.append("Fizz")
    #         elif not i % 5:
    #             res.append("Buzz")
    #         else:
    #             res.append(str(i))
    #     return res

    # when the number of conditions grows
    def fizzBuzz(self, n: int) -> List[str]:
        fb_dict = {3: "Fizz", 5: "Buzz"}

        res = list()
        for i in range(1, n + 1):
            ele = ""
            for num, string in fb_dict.items():
                if not i % num:
                    ele += string
            if len(ele) == 0:
                ele = str(i)
            res.append(ele)

        return res

# @lc code=end

