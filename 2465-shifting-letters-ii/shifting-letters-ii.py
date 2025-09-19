class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        diff = [0] * n

        for start, end, direction in shifts:
            if direction == 0:
                diff[start] += -1
                if end + 1 < n:
                    diff[end+1] += 1 # diff[end+1] -= -1
            
            if direction == 1:
                diff[start] += 1
                if end + 1 < n:
                    diff[end+1] -= 1

        shift = 0
        ans = []
        for i in range(n):
            shift += diff[i]
            actual_shift = (ord(s[i]) - ord('a') + shift) % 26
            ans.append(chr(ord('a') + actual_shift))

        return ''.join(ans)

        


        # n = len(s)
        # indexes = [0] * n

        # for start, end, direction in shifts:
        #     if direction == 0:
        #         for i in range(start, end + 1):
        #             indexes[i] -= 1
            
        #     if direction == 1:
        #         for i in range(start, end + 1):
        #             indexes[i] += 1

        # ans = ''
        # for i in range(n):
        #     new_char = ord(s[i]) - ord('a') + indexes[i]
        #     if new_


