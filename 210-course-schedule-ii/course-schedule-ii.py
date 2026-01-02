from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        kahn's algo (BFS)
        '''
        n = numCourses
        q = deque()
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        for course in range(n):
            if indegree[course] == 0:
                q.append(course)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for course in adj[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        if len(res) != n:
            return []

        return res
