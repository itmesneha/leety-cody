class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        def is_exit(position):
            x, y = position
            if x == 0 or y == 0 or x == rows -1 or y == cols - 1:
                if [x,y] != entrance and maze[x][y] != '+':
                    return True
            return False

        def check(position):
            x, y = position
            if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == '+':
                return False
            return True

        queue = []
        queue.append((entrance, 0))
        directions = [[0,1], [0, -1], [1,0], [-1, 0]]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while queue:
            position, current_steps = queue.pop(0)
            if is_exit(position):
                # steps number ???
                return current_steps
            for direction in directions:
                new_position = (position[0] + direction[0] , position[1] + direction[1])
                if new_position in visited:
                    continue
                if check(new_position):
                    visited.add(new_position)
                    queue.append((new_position, current_steps + 1))
                # else:
                    
        return -1






        # rows = len(maze)
        # cols = len(maze[0])
        # start_x = entrance[0]
        # start_y = entrance[1]
        # visited = set()
        # def fn(x, y, visited):
        #     if (x,y) in visited:
        #         return float('inf')
        #     if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == '+':
        #         return float('inf')
        #     if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
        #         if maze[x][y] != '+' and [x,y] != entrance:
        #             return 1
        #     visited.add((x,y))
        #     left = 1 + fn(x-1, y, visited)
        #     right = 1 + fn(x + 1, y, visited)
        #     up = 1 + fn(x, y - 1, visited)
        #     down = 1 + fn(x, y + 1, visited)
        #     visited.remove((x,y))
        #     return min(left, right, up, down)

        # ans = fn(start_x, start_y, visited)
        # return ans if ans != 0 else -1