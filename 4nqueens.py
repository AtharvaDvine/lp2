def print_solution(board): 
    for row in board: 
        print(" ".join("Q" if cell else "." for cell in row)) 
    print("\n") 

def is_safe(row, col, left_row, upper_diag, lower_diag, N): 
    return not left_row[row] and not upper_diag[row + col] and not lower_diag[row - col + N - 1] 

def solve_nqueens(board, col, left_row, upper_diag, lower_diag, N): 
    if col >= N: 
        print_solution(board) 
        return True 

    found = False 
    for i in range(N): 
        if is_safe(i, col, left_row, upper_diag, lower_diag, N): 
            board[i][col] = 1 
            left_row[i] = upper_diag[i + col] = lower_diag[i - col + N - 1] = True 
            
            found = solve_nqueens(board, col + 1, left_row, upper_diag, lower_diag, N) or found 
            
            
            board[i][col] = 0 
            left_row[i] = upper_diag[i + col] = lower_diag[i - col + N - 1] = False 

    return found 

def nqueens(): 
    N = int(input("Enter the value of N: ")) 
    board = [[0] * N for _ in range(N)] 
    left_row = [False] * N 
    upper_diag = [False] * (2 * N - 1) 
    lower_diag = [False] * (2 * N - 1) 
    
    if not solve_nqueens(board, 0, left_row, upper_diag, lower_diag, N): 
        print("No solution exists") 

nqueens()
