class Solution:
    def minPathSum(self, grid):
        y = len(grid) #y
        x = len(grid[0]) # x
        
        dp = [x[:] for x in [[0] * x] * y]
        dp[0][0] = grid[0][0]
        
        if(x != 1):
            ty = 0;
            tx = 1;
        elif(y!=1):
            ty = 1;
            tx = 0;
        else:
            return grid[0][0]
        
        while(True):
            if(ty -1 >= 0 and tx -1 >= 0):
                dp[ty][tx] = grid[ty][tx] + min(dp[ty-1][tx],dp[ty][tx-1])
            elif(ty-1<0):
                dp[ty][tx] = grid[ty][tx] + dp[ty][tx-1]
            else:
                dp[ty][tx] = grid[ty][tx] + dp[ty-1][tx]
            
                
            
            if (tx == x -1):
                tx = 0
                ty+=1     
                if (ty == y):
                    break
            else:
                tx += 1
            
                
        return dp[y-1][x-1]
        
        
        
        print(dp)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
