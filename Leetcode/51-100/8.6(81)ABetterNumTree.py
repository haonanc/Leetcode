#Time complexity O(n)
class Solution:
    def numTrees(self, n):
        dp = [1,1] + [-1]*n
        ans = 0
        for i in range(1,n+1):
            ans += recursion(dp,i-1)*recursion(dp,n-i)
        return ans
            
def recursion(dp,num):
    if dp[num] == -1:
        temp = 0
        for i in range(1,num+1):
            temp += recursion(dp,i-1)*recursion(dp,num-i)
        dp[num] = temp
        return temp
    else:
        return dp[num]
            
        """
        :type n: int
        :rtype: int
        """
        
    
        
