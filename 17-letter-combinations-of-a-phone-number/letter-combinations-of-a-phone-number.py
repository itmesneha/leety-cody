class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        self.res = []
        def fn(idx1, ans):
            if idx1 == len(digits):
                if len(ans) > 0:
                    self.res.append(ans)
                return
            if idx1 > len(digits):
                return
            for letter in self.dic[digits[idx1]]:
                fn(idx1 + 1, ans + letter)
        fn(0, '')
        return self.res