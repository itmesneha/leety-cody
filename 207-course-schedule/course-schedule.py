from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Kahn's Algorithm for topological sort
        1. first calculate adjacency matrix (dictionary node --> connections) and indegrees
        2. put nodes with indegree = 0 in deque
        3. while q:
            pop from q
            append to result
            add to count + 1
            for each connection:
                subtract 1 from indegree
                if for that node indegree == 0:
                    append to deque

        4. if count == n then no cycle, else cycle (no topoligcal sort)
        '''

        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for neighbor in adj[cur]:
                indegree[neighbor] -=1 
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if count == numCourses:
            return True

        return False

