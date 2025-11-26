class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        2 pointers
        convert all to lowercase
        while iterating if char < ord('a') or char > ord('z') continue (non-alphanumeric)
        '''
        def isValidChar(char):
            if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
                return True
            return False

        left = 0
        n = len(s)
        right = n-1
        s = s.lower()
        while left < right:
            while left < right and not isValidChar(s[left]) :
                left += 1
            while left < right and not isValidChar(s[right]):
                right -= 1
            # print(s[left], s[right])
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

