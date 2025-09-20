from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = deque()
        # append first interval to ans list
        ans.append(intervals[0])
        # iterate through rest of list
        for i in range(1, n):

            # if last ans end has not ended and next event has started need to merge
            if ans[-1][1] >= intervals[i][0]:
                # remove last one and create merged interval
                start, end = ans.pop()
                new_start = min(start, intervals[i][0])
                new_end = max(end, intervals[i][1])

                ans.append([new_start, new_end])
                

            else:
                ans.append(intervals[i])

        return list(ans)



