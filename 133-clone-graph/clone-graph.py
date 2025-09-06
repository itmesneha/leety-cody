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
        if not node:
            return None
        map = {}
        def dfs(cur):
            if cur.val in map:
                return map[cur.val]
            
            copy = Node(cur.val, [])
            map[cur.val] = copy
            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)