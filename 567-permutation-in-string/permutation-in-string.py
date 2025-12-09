class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        fixed length sliding window + use 26 size list to store alphabet counts
        '''
        cs1, cs2 = [0] * 26,[0] * 26
        for x in s1:
            cs1[ord(x)-ord('a')] += 1 # stores character frequencies at indices

        l = 0
        r = len(s1) - 1 # fixed window size
        
        for x in s2[l:r+1]:
            cs2[ord(x)-ord('a')] += 1

        while r < len(s2):
            if cs1 == cs2:
                return True

            # slide fixed variable window to right
            cs2[ord(s2[l]) - ord('a')] -= 1 # subtract count for left character
            l += 1
            r += 1
            if r < len(s2):
                cs2[ord(s2[r]) - ord('a')] += 1 # add count for right character if within range

        return False
