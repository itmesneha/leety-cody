class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        From each index, try every palindromic prefix and recurse on the suffix.
        for loop is for breadth
        recursion is for depth
        For-loop explores all cut choices at the current index;
        recursion goes deeper on the remaining  suffix.
        '''
        def isPalindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1
            
            return True

        
        n = len(s)
        self.res = []
        def fn(start, li):
            if start == n:
                self.res.append(li[:])
                return

            for end in range(start, n):
                if isPalindrome(s[start:end+1]):
                    li.append(s[start:end+1])
                    fn(end+1, li)
                    li.pop()

        fn(0, [])
        return self.res
