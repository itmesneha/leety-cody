from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Cannot use Kahn's algo here:
        Why indegree logic breaks for undirected graphs:
            In a tree:
                Every node except leaves has indegree ≥ 1
                Leaves have indegree = 1 (not 0)

        An undirected graph is a tree iff:
            - Connected
            - No cycles
            - edges = n - 1

        You only need two checks:
            - len(edges) == n - 1
            - graph is connected

        n - 1 edges ⇒ no cycles possible
        BFS reaching all nodes ⇒ connected
        Connected + no cycles ⇒ tree
        '''
        if len(edges) != n-1:
            return False 
            
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            cur = q.popleft()
            for neighbor in adj[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)


        if len(visited) == n:
            return True

        return False




