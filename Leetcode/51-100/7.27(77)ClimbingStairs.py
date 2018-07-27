class Solution:
    def climbStairs(self, n):
        dp = {1:1,2:2}
        recursion(n,dp)
        return dp[n]
        """
        :type n: int
        :rtype: int
        """
def recursion(n,dp):
    if n in dp.keys():
        return dp[n]
    else:
        dp[n] = recursion(n-1,dp) + recursion(n-2,dp)
        return dp[n]
        
