class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # found the row
                row = matrix[mid]
                left, right = 0, len(row)-1
                while left <= right:
                    m = (left+right)//2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        left = m+1
                    else:
                        right = m-1
                return False
            elif matrix[mid][-1] < target:
                top = mid+1
            else:
                bottom = mid-1
        return False