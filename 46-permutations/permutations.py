class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def fn(idx):
            if idx == n:
                res.append(nums[:])
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                fn(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        fn(0)
        # def fn(cur, used):
        #     if len(cur) == n:
        #         res.append(cur[:])
        #         return
        #     for i in range(n):
        #         if i in used: # for duplicate numbers also this will work
        #             continue
        #         used.add(i)
        #         cur.append(nums[i])
        #         fn(cur, used)
        #         used.remove(i)
        #         cur.pop()

        # fn([], set())
        return res