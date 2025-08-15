class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 0:
            return False
        if n % 10 in [1,3,9,7]:
            while n != 1:
                if n % 3 == 0:
                    n = n // 3
                else:
                    return False
            return True
        return False