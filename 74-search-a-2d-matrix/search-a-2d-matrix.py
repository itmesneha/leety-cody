class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        first do a search on columns
        once find correct col do search on rows
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        row_to_search = -1
        for row in range(rows):
            if matrix[row][0] <= target <= matrix[row][cols-1]:
                row_to_search = row
                break

        if row_to_search == -1:
            return False

        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row_to_search][mid] == target:
                return True
            elif target < matrix[row_to_search][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False