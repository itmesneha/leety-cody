class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        for i in range(1, len(num) - 1):
            if num[i] == num[i-1] == num[i+1]:
                if res == '' or num[i] > res[0]:
                    res = num[i-1 : i + 2]
        return res