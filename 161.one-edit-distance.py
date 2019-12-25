# # O(n) and O(1)
# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if abs(len(s) - len(t)) > 1:
#             return False

#         if len(s) == len(t):
#             count = 0
#             for i in range(len(s)):
#                 if s[i] != t[i]:
#                     count += 1
#                     if count > 1:
#                         return False
#             return count == 1

#         if len(s) > len(t):
#             s, t = t, s
#         i = j = 0
#         count = 0
#         while i < len(s):
#             if s[i] != t[j]:
#                 count += 1
#                 if count > 1:
#                     return False
#             else:
#                 i += 1
#             j += 1
#         return True


# more concise answer
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return len(s) + 1 == len(t)
