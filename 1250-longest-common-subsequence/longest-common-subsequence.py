class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        memo = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        def fn(idx1, idx2):
            if idx1 == n1 or idx2 == n2:
                return 0
            if memo[idx1][idx2] != -1:
                return memo[idx1][idx2]
            ans = 0
            if text1[idx1] == text2[idx2]:
                ans = 1 + fn(idx1 + 1, idx2 + 1)
            else:
                ans = max(fn(idx1 + 1, idx2), fn(idx1, idx2 + 1))
            memo[idx1][idx2] = ans
            return memo[idx1][idx2]

        return fn(0, 0)