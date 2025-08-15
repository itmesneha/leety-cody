class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        max_pow = 4 ** 15
        return n > 0 and n % 10 in [1, 4,6] and max_pow % n == 0