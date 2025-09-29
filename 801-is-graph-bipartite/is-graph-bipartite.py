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

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True