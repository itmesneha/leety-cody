"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Use a hashmap to map original nodes to cloned nodes, and DFS to rebuild neighbors.
        '''

        visited = {}

        def dfs(cur):
            if not cur:
                return None

            if cur in visited:
                return visited[cur] # have to return copied graph here

            # created copy
            newcur = Node(cur.val)

            # saved the copy mapping in dictionary
            visited[cur] = newcur

            for neighbor in cur.neighbors:
                newcur.neighbors.append(dfs(neighbor))

            return newcur

        return dfs(node)

        
