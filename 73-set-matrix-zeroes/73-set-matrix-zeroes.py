class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row,col = set(),set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for r in row:
            matrix[r] = [0] * n
            
        for c in col:
            for i in range(m): 
                matrix[i][c] = 0