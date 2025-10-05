class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1

        parent = [0] * n
        rank = [0] * n

        for i in range(n):
            parent[i] = i

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            x_p = find(x)
            y_p = find(y)

            if rank[x_p] > rank[y_p]:
                parent[y_p] = x_p
            elif rank[x_p] < rank[y_p]:
                parent[x_p] = y_p
            else:
                parent[x_p] = y_p
                rank[y_p] += 1

        components = n
        for u, v in connections:
            p_u = find(u)
            p_v = find(v)
            if p_u != p_v:
                union(p_u, p_v)
                components -= 1
            
        return components - 1