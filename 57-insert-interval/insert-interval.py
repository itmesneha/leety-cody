class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        n = len(intervals)

        new_start, new_end = newInterval

        # add all intervals before new interval
        while i < n and intervals[i][1] < new_start: # end < new start
            res.append(intervals[i]) # need to append whichever one comes first
            i += 1

        # add merged intervals
        while i < n and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i+= 1

        res.append([new_start, new_end])


        # add all intervals after new interval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        