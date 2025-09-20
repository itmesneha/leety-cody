class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # curstart = intervals[0][0]
        curend = intervals[0][1]
        n = len(intervals)
        count = 0
        for i in range(1, n):
            if curend > intervals[i][0]: # overlap
                if intervals[i][1] < curend: # keeping the one that ends first
                    curend = intervals[i][1]
                    # curstart = intervals[i][0]

                count += 1
            else:
                # curstart = intervals[i][0]
                curend = intervals[i][1]

        return count
