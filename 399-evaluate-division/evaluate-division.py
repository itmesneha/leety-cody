class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        n = len(values)
        for i in range(n):
            u,v = equations[i]
            val = values[i]
            adj[u].append((v,val))
            adj[v].append((u,(1/val)))
        
        res = []

        def dfs(start, end, product, visited):
            if start == end:
                return product
            visited.add(start)
            for child, value in adj[start]:
                if child not in visited:
                    result = dfs(child, end, product * value, visited)
                    if result != -1:
                        return result
            return -1
        
        for start, end in queries:
            if start not in adj or end not in adj:
                res.append(-1.0)
            else:
                visited = set()
                res.append(dfs(start, end, 1, visited))

        return res
        