class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Word Break = DP on index; try all words at each cut.
        If the first valid prefix leads to a dead end, you must backtrack and try another prefix.
        '''

        memo = {}
        def fn(s):
            if s in memo:
                return memo[s]
            if s in wordDict:
                memo[s] = True
                return memo[s]
            for i in range(len(s)+1):
                if s[:i] in wordDict and fn(s[i:]):
                    memo[s] = True
                    return memo[s]

            memo[s] = False
            return memo[s]

                # this is wrong:
                # because if s = 'carscar' and wordDict = ['car', 'cars']
                # then it will find 'car' first and the remaining 'scar' will fail
                # and it will return false

                # we also need it to fail and come back and find 'cars' first then 'car'
                # then return true
                # if s[:i] in wordDict:
                #     return fn(s[i:])

        if fn(s):
            return True
        return False
