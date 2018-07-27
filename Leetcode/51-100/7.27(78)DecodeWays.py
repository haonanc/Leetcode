class Solution:
    def numDecodings(self, s):
        if(s[0] =='0'):
            return 0
        dp = {-1:1,0:1}
        recursion(s,dp,len(s)-1)
        if(-2 in dp.keys()):
            return 0
        return dp[len(s)-1]
        """
        :type s: str
        :rtype: int
        """
def recursion(s,dp,counter):

    if counter in dp.keys():
        return dp[counter]
    else:
        if s[counter] == '0' and(int(s[counter-1]+s[counter]) > 26 or s[counter-1] == '0'):
            dp[-2] = 0
            return 0
        elif int(s[counter-1]+s[counter]) > 26:
            dp[counter] =  recursion(s,dp,counter-1)
        elif s[counter-1] == '0':
            dp[counter] =  recursion(s,dp,counter-1)
        elif s[counter] == '0':
            dp[counter] =  recursion(s,dp,counter-2)
        else:
            dp[counter] =  recursion(s,dp,counter-2) + recursion(s,dp,counter-1)

        return dp[counter]
            

            
       
            
            
