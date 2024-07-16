class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowlen = len(matrix[0])
        collen = len(matrix)
        low = 0 
        high = rowlen * collen - 1
        while low <= high:
            mid = (low + high)//2
            row = mid // rowlen
            col = mid % rowlen
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
