class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        memo = [-1 for _ in range(n+1)]
        memo_palindrome = [[None for _ in range(n+1)] for _ in range(n+1)]
        def isPalindrome(i, j):
            if i > j:
                return True
            if memo_palindrome[i][j] != None:
                return memo_palindrome[i][j]
            if s[i] != s[j]:
                return False
            memo_palindrome[i][j] = isPalindrome(i+1, j-1)
            return memo_palindrome[i][j]

        def fn(idx):
            nonlocal count
            if idx == n:
                return
            if memo[idx] != -1:
                return memo[idx]
            for j in range(idx, n):
                if isPalindrome(idx, j):
                    count += 1
            memo[idx] = count
            fn(idx + 1)

        fn(0)
        return count