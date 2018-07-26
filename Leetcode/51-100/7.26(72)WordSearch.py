class Solution:
    def exist(self, board, word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if(backtrace(y,x,board,word)):
                    return True
        return False
        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
def backtrace(y,x,board,word):
    if(y >= len(board) or x >= len(board[0]) or x < 0 or y < 0):
        return False

    if(board[y][x] == word[0]):
        temp = word[0]
        board[y][x] = " "
        if(len(word[1:]) == 0):
            return True
        if(backtrace(y-1,x,board,word[1:]) or backtrace(y,x-1,board,word[1:]) or backtrace(y,x+1,board,word[1:]) or backtrace(y+1,x,board,word[1:])):
            return True
        board[y][x] = temp
    return False
    
        
