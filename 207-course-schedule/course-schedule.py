from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for v,u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            cur = q.pop()
            count += 1
            for child in adj[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        return count == numCourses