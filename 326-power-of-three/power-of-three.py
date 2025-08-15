# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n == 0:
#             return False
#         if n % 3 == 0:
#             return self.isPowerOfThree(n / 3)
#         return False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_pow = 1162261467
        return n > 0 and max_pow % n == 0