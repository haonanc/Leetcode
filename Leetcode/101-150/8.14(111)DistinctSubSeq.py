class Solution(object):
    def numDistinct(self, s, t):
        
        sLen,tLen = len(s),len(t)
        if not tLen:
            return 1
        if not sLen:
            return 0
        
        dp = [[1]*(sLen+1) for y in range(tLen+1)]
        
        for y in range(1,tLen+1):
            for x in range(1,sLen+1):
                if x == y:
                    if s[:x] == t[:y]:
                        dp[y][x] = 1
                    else:
                        dp[y][x] = 0
                elif y > x:
                    dp[y][x] = 0
                else:
                    if s[x-1] == t[y-1]:
                        dp[y][x] = dp[y][x-1] + dp[y-1][x-1]
                    else:
                        dp[y][x] = dp[y][x-1]
        return dp[tLen][sLen]
        """
        :type s: str
        :type t: str
        :rtype: int
        """
