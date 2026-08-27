class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = list()
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # left -> right traversal
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1

        # top -> bottom traversal
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:    
            # right -> left traversal
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # bottom -> top traversal
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return res