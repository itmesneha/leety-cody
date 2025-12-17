class Solution:
    def letterCombinations(self, nums: str) -> List[str]:
        self.dic = {'2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        self.res = []
        n = len(nums)
        def fn(idx, op):
            if idx == n:
                self.res.append(op)
                return

            for val in self.dic[nums[idx]]:
                # op.append(val)
                fn(idx + 1, op + val)
                # op.pop()


        fn(0, '')
        return self.res
