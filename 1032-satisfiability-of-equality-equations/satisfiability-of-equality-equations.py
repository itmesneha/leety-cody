from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [''] * 26
        rank = [0] * 26

        for i in range(26):
            parent[i] = i

        def find(i):
            if i == parent[i]:
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

        # equal cases
        for equation in equations:
            if equation[1] != '!':
                x = equation[0]
                y = equation[3]
                union(ord(x) - ord('a'), ord(y) - ord('a'))

        # not equal cases & check validity
        for equation in equations:
            if equation[1] == '!':
                x = equation[0]
                y = equation[3]

                x_p = find(ord(x) - ord('a'))
                y_p = find(ord(y) - ord('a'))

                if x_p == y_p:
                    return False
                
        return True