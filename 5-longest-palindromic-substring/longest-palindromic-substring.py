class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        expand around center
        for even length palindromes, center = i, i + 1
        for odd = i

        around the center keep expanding and checking equality, 
        once inequality reached return max left and max right for max length
        '''

        n = len(s)
        res = ''

        def expand(left, right):
            nonlocal res
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right+1]
                left -= 1
                right += 1

        
        for i in range(n):
            expand(i,i)
            expand(i, i+1)

        return res


        