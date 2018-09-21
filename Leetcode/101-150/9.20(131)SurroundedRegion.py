class Solution:
    def solve(self, board):
        if len(board) == 0:
            return 
        if len(board[0]) == 0:
            return
        bfs = []
        for y in range(0,len(board)):
            for x in range(0,len(board[0])):
                if ((y in [0,len(board)-1] or x in [0,len(board[0])-1]) and board[y][x] == 'O'):
                    bfs.append([y,x])
        while bfs:
            y,x = bfs[0][0],bfs[0][1]
            if y >= 0 and x >= 0  and y < len(board) and x < len(board[0]):
                if board[y][x] == 'O':
                    board[y][x] = 'S'
                    bfs.append([y+1,x])
                    bfs.append([y-1,x])
                    bfs.append([y,x+1])
                    bfs.append([y,x-1])                  
            del bfs[0]
        for y in range(0,len(board)):
            for x in range(0,len(board[0])):
                if board[y][x] == "S":
                    board[y][x] = 'O'
                elif board[y][x] =="O":
                    board[y][x] = 'X'
        
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
