class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        res = []
        n = len(s)
        end = 0 
        start = 0
        last = {c: i for i,c in enumerate(s)}
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
