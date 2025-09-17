class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        m = len(image)
        n = len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
        def fn(i, j):
            if i < 0 or i == m or j < 0 or j == n: # out of bounds
                return
            if image[i][j] != start_color:
                return
            image[i][j] = color
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                fn(ni, nj)
        fn(sr, sc)
        return image


