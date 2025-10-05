class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [0] * n
        rank = [0] * n

        # initialize every node to have itself as parent
        for i in range(n):
            parent[i] = i
        
        # find leader of ilaka 
        def find(i):
            if parent[i] == i:
                return i
            parent[i]= find(parent[i])
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

        for u,v in edges:
            p_u = find(u)
            p_v = find(v)

            if p_u != p_v:
                union(u, v)

        hashmap = defaultdict(int)

        for i in range(n):
            hashmap[find(i)] += 1

        print(hashmap)
        remaining = n
        result = 0
        for component in hashmap:
            size = hashmap[component]
            result += size * (remaining - size)
            remaining -= size

        return result


