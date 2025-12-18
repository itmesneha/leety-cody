from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        '''
        Max frequency creates gaps, others fill them, leftover gaps become idle.
        '''
        from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        try to complete the tasks that have largest frequency first

        '''
        freq = Counter(tasks)
        print(freq)
        maxfreq = max(freq.values())
        empty_blocks = maxfreq-1
        idle_spots = empty_blocks * n
        count = 1
        for task in freq:
            if freq[task] == maxfreq and count == 1:
                count -= 1
            else:
                idle_spots -= min(freq[task], empty_blocks)

        if idle_spots > 0:
            return len(tasks) + idle_spots

        else:
            return len(tasks)


        return max(len(tasks), cost)
