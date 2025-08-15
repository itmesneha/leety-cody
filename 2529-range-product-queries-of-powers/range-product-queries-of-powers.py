class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = (10 ** 9) + 7
        for i in range(32):
            if n & (1 << i) != 0:
                powers.append(2**i)
        pre = []
        temp = 1
        for i in range(len(powers)):
            temp *= powers[i]
            pre.append(temp)
        # print(pre)
        ans = []
        for [start, end] in queries:
            if start == 0:
                den = 1
            else:
                den = pre[start - 1]
            ans.append((pre[end] // den) % mod)
        return ans
