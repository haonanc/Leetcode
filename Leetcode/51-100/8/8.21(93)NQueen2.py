class Solution(object):
    def totalNQueens(self, n):
        board = [[False]*n for _ in range(n)]
        return backtracking(board,0)
        
    
def backtracking(board,y):
    if y == len(board):
        return 1
    ans = 0
    for x in range(len(board)):
        b = False
        for dy in range(y):
            if board[dy][x]:
                b = True
                break
        for dy in range(y):
            if x-1-dy > -1:
                if board[y-1-dy][x-1-dy]:
                    b = True
                    break
            if x+1+dy < len(board):
                if board[y-1-dy][x+1+dy]:
                    b = True
                    break
        if b:
            continue                       
        board[y][x] = True
        ans += backtracking(board,y+1)
        board[y][x] = False
    return ans
        
