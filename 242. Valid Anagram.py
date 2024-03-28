class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(sorted(s))
        # print(sorted(t))
        # print(sorted(s) == sorted(t))
        return sorted(s) == sorted(t)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         letters1 = list()
#         letters2 = list()
#         for i in s:
#             letters1.append(i)
#         for i in t:
#             letters2.append(i)
#         # print(letters1.sort())
#         # print(letters2.sort())
#         if sorted(letters1) == sorted(letters2):
#             return True
#         else:
#             return False
