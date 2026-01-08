class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        expand around center
        duplicates allowed so just keep count variable
        '''

        n = len(s)
        count = 0
        
        def expand(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            count += expand(i,i)
            count += expand(i,i+1)

        return count

        