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
            temp = (temp * powers[i]) % mod
            pre.append(temp)
        # print(pre)
        # (a/b)modm != (amodm)/(bmodm) 
        # (a/b)modm≡a⋅b−1modm
        ans = []
        for [start, end] in queries:
            if start == 0:
                den = 1
            else:
                den = pre[start - 1]
            ans.append((pre[end] * pow(den, -1, mod)) % mod)
        return ans
