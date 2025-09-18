from functools import lru_cache
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        # print(events)

        def binarySearch(index, end_index):
            l = index + 1
            r = n - 1
            result = n
            while l <= r :
                mid = (l+r) // 2 
                if events[mid][0] > end_index:
                    result = mid
                    r = mid -1
                else:
                    l = mid + 1

            return result

        @lru_cache(None)
        def solve(index, count):
            if count == 2 or index >= n:
                return 0

            nextValidIndex = binarySearch(index, events[index][1])  # end index
            take = events[index][2] + solve(nextValidIndex, count + 1)
            
            not_take = solve(index + 1, count)

            return max(take, not_take)

        return solve(0, 0)