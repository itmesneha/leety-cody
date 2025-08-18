class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res = res + str(len(word)) + '#'
            res = res + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = ''
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i : j])
            res.append(s[j + 1:j + 1 + count])
            i = j + 1 + count
        return res

