class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [None for _ in range(n + 1)]
        def fn(idx):
            if idx >= n:
                return True
            if memo[idx] != None:
                return memo[idx]
            for length in range(1, n - idx + 1):
                # print(s[idx : idx + length])
                if s[idx : idx + length] in wordDict:
                    if fn(idx + length): # don’t return immediately, check all
                        memo[idx] = True
                        return True
                    # print('found')
            memo[idx] = False
            return False

        return fn(0)