class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        options = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        
        
        def isValid(board, r, c, option):
            
            for i in range(9):
                if board[r][i] == option:
                    return False
                if board[i][c] == option:
                    return False
                if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == option:
                    return False
            
            return True
        
        
        
        def solve(board, i, j):

            
            if j == 9:
                return solve(board, i+1, 0)
            
                        
            if i == 9:
                return True
            
            if board[i][j] != '.':
                return solve(board, i , j+1)
            
            
            for option in options:
                
                if isValid(board, i, j, option):
                    
                    board[i][j] = option
                    if solve(board, i, j+1):
                        return True
                    board[i][j] = '.'
                    
            return False
        
        
        solve(board,0,0)