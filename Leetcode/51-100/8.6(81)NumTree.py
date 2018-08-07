class Solution:
    def numTrees(self, n):
        dp = [1,1]
        for p in range(2,n+1):
            temp = 0
            for i in range(1,p+1):
                temp += dp[i-1]*dp[p-i]
            dp.append(temp)
        return dp[n]
            
