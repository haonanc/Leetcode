class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [x[:] for x in [[0] * m] * n]
        dm = 0
        dn = 0
        dp[0][0] = 1
        
        while(True):
            if(obstacleGrid[dn][dm] == 1):
                dp[dn][dm] = 0
            else:
                if(dm - 1 >= 0 and dn - 1 >= 0):
                    dp[dn][dm] = dp[dn-1][dm] + dp[dn][dm-1]
                elif(dm - 1 >= 0):
                    dp[dn][dm] = dp[dn][dm-1]
                elif(dn - 1 >= 0):
                    dp[dn][dm] = dp[dn-1][dm]
                else: 
                    dp[dn][dm] = 1

            if(dn == n - 1):
                dn = 0
                dm += 1 
                if(dm >= m):
                    break
            else:
                dn += 1
        
        return dp[n-1][m-1]
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
