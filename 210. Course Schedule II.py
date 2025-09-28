from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for child in adj[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        if len(res) == numCourses:
            return res
        else:
            return []
