class Solution:
    def uniquePaths(self, m, n):
        
        dp = [x[:] for x in [[0] * m] * n]
        dm = 0
        dn = 0
        dp[0][0] = 1
        
        while(True):
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
        :type m: int
        :type n: int
        :rtype: int
        """
        
