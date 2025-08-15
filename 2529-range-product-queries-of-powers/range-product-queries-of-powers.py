class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = (10 ** 9) + 7
        for i in range(32):
            if n & (1 << i) != 0:
                powers.append(2**i)
        # print(powers)
        ans = []
        for [start, end] in queries:
            res = 1
            for i in range(start, end + 1):
                res *= powers[i] % mod
            ans.append(res % mod)
        return ans
