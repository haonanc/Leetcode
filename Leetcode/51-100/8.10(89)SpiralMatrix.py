class Solution:
    def generateMatrix(self, n):
        toRet = [[0]*n for x in range(n)]
        y,x,cy,cx = 0,-1,0,1
        helper = [n,2*n-1,3*n-2]

        for i in range(1,n**2+1):
            
            y += cy
            x += cx
            toRet[y][x] = i
            
            if i not in helper:
                if toRet[y+cy][x+cx] == 0:
                    continue         
            if cx == 0:
                cx = -cy
                cy = 0
            else:
                cy = cx
                cx = 0
            

        return toRet
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
