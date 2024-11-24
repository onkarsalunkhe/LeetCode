class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        neg = []
        minSum = float('inf')
        sum = 0
        for i in range(row):
            for j in range(col):

                if matrix[i][j] < 0:
                    sum += -matrix[i][j]
                    minSum = min(minSum, -matrix[i][j])
                    neg.append(matrix[i][j])    
                else:
                    sum += matrix[i][j]
                    minSum = min(minSum, matrix[i][j])

        if len(neg) % 2 == 0: 
            return sum
        else:
            return sum - 2*minSum