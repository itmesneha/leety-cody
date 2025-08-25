class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        # memo = [-1 for _ in range(n+1)]
        # memo_palindrome = [[None for _ in range(n+1)] for _ in range(n+1)]
        # def isPalindrome(i, j):
        #     if i > j:
        #         return True
        #     if memo_palindrome[i][j] != None:
        #         return memo_palindrome[i][j]
        #     if s[i] != s[j]:
        #         return False
        #     memo_palindrome[i][j] = isPalindrome(i+1, j-1)
        #     return memo_palindrome[i][j]

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return count