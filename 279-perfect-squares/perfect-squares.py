class Solution:
    def numSquares(self, n: int) -> int:

        # if n itself is a square
        if int(sqrt(n)) ** 2 == n:
            return 1

        # check if can be sum of 2 squares
        for i in range(1, int(sqrt(n)) + 1):
            rem = n - (i*i)
            c = int(sqrt(rem))
            if c*c == rem:
                return 2

        # check if can be sum of 3 squares
        for i in range(1, int(sqrt(n)) + 1):
            for j in range(1, int(sqrt(n-(i*i))) + 1):
                rem = n - (i*i) - (j*j)
                c = int(sqrt(rem))
                if c*c == rem:
                    return 3

        return 4


        # memo = [-1] * (num+1)
        # squares = [-1] * 101
        # # for i in range(10000):
        # #     squares.append(i**2)
            
        # def fn(n):
        #     if n == 0:
        #         return 0
        #     if memo[n] != -1:
        #         return memo[n]
        #     i = 1
        #     res = float('inf')
        #     while i <= sqrt(n):
        #         if squares[i] == -1:
        #             squares[i] = i**2
        #         square_value = squares[i]
        #         res = min(res, 1+fn(n-square_value))
        #         i += 1
        #     memo[n] = res
        #     return res

        # return fn(num)