class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        n = len(s)
        
        def sliding_window(cur):
            l = 0
            r = 0
            consecutive = 0
            count = 0
            while r < n:
                if s[r] != cur:
                    count += 1
                    while count > k:
                        if s[l] != cur:
                            count -= 1
                        l += 1

                consecutive = max(consecutive, r - l+1)
                r += 1
            return consecutive

        return max(sliding_window('T'), sliding_window('F'))