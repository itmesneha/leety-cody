class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        pre = 0
        res = []
        for i in range(n-1, -1, -1):
            pre += shifts[i]
            total_shift = (ord(s[i]) - ord('a') + pre) % 26 # [0-25]
            res.append(chr(ord('a') + total_shift))

        return ''.join(res[::-1])

        # difference array technique

        
        # diff = [0] * n
        # for i in range(n):
        #     diff[0] += shifts[i]
        #     if i + 1 < n:
        #         diff[i + 1] -= shifts[i]

        # shift = 0
        # res = []
        # for i in range(n):
        #     shift += diff[i]
        #     total_shift = (ord(s[i]) - ord('a') + shift) % 26 # [0-25]
        #     res.append(chr(ord('a') + total_shift))

        
