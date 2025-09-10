from collections import deque
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for v, u in pre:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        # print('q: ', q)
        nodecount = 0
        while q:
            cur = q.popleft()
            # print('q: ', q)
            for child in adj[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            nodecount += 1
            # print('nodecount: ', nodecount)

        return nodecount == n # no cycle therefore can take course , else not.