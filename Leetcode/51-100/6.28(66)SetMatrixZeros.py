class Solution:
    def setZeroes(self, matrix):
        x = len(matrix[0])
        y = len(matrix)
        self.recursion(0,0,matrix)
        
        
        
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    def recursion(self,x,y,matrix):
        ny = y
        if(x+1 == len(matrix[0])):
            nx = 0
            ny = y + 1
        else:
            nx = x + 1
        if(matrix[y][x] == 0):
            b = True
        else:
            b = False
        if(ny != len(matrix)):
            self.recursion(nx,ny,matrix)
     
        if(b):
            for i in range(0,len(matrix[0])):
                matrix[y][i] = 0
            for i in range(0,len(matrix)):
                matrix[i][x] = 0
            
        
        
        
        
        
