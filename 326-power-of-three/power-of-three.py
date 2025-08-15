class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_pow = 3 ** 19
        return n > 0 and max_pow % n == 0