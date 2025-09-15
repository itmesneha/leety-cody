class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def fn(cur, used):
            if len(cur) == n:
                res.append(cur[:])
                return
            for i in range(n):
                if i in used: # for duplicate numbers also this will work
                    continue
                used.append(i)
                cur.append(nums[i])
                fn(cur, used)
                used.pop()
                cur.pop()

        fn([], [])
        return res