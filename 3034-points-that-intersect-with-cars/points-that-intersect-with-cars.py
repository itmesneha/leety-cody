class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        covered = set()

        for start, end in nums:
            for i in range(start, end + 1):
                covered.add(i)

        return len(covered)

        # starts = []
        # ends = []
        # for start, end in nums:
        #     starts.append(start)
        #     ends.append(end)

        # starts.sort()
        # ends.sort()

        # i = 1
        # j = 0
        # points = 1
        # n = len(nums)

        # while i < n and j < n:
        #     if starts[i] < ends[i]:
        #         points += 1
        #         i += 1
        #     else:
        #         j += 1

        # return points
