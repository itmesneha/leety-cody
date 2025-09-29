from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(cur, cur_color):
            color[cur] = cur_color
            for child in graph[cur]:
                if color[child] == cur_color:
                    return False
                if color[child] == -1:
                    if not dfs(child, 1 - cur_color):
                        return False

            return True

        def bfs(cur, cur_color):
            color[cur] = cur_color
            q = deque()
            q.append(cur)
            while q:
                node = q.popleft()
                for child in graph[node]:
                    if color[child] == color[node]:
                        return False
                    if color[child] == -1:
                        color[child] = 1 - color[node]
                        q.append(child)

            return True

        for i in range(n):
            if color[i] == -1:
            # this does not matter whether i start from 0 or 1 
            # because this is for disconnected parts of the graph
                if not bfs(i, 0): 
                    return False
        return True