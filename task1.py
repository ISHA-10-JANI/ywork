def solve_sudoku(board):
    def is_valid(board, row, col, num):
        num_str = str(num)
        
        # Check row
        for j in range(9):
            if board[row][j] == num_str:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num_str:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num_str:
                    return False
        
        return True
    
    def find_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return None, None
    
    def backtrack():
        row, col = find_empty_cell(board)
        
        if row is None:
            return True
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = str(num)
                
                if backtrack():
                    return True
                
                board[row][col] = '.'
        
        return False
    
    return backtrack()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
