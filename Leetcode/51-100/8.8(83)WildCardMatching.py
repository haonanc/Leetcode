class Solution:
    def isMatch(self, s, p):
        lenRegEx = len(p)
        lenStr = len(s)
        dp = [[False ]*(lenStr+1) ]*(lenRegEx+1)
        dp[0][0] = True
        for y in range(lenRegEx):
            if p[y] == "*":
                dp[y+1][0] = dp[y][0]
            else:
                dp[y+1][0] = False
        for y in range(lenRegEx):
            for x in range(lenStr):
                if s[x] == p[y] or p[y] == "?":
                    dp[y+1][x+1] = dp[y][x]
                elif p[y] == "*":
                    dp[y+1][x+1] = (dp[y][x+1] or dp[y+1][x])
                else:
                    dp[y+1][x+1] = False
        return dp[lenRegEx][lenStr]
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
