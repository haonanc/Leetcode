class Solution:
    def isInterleave(self, s1, s2, s3):
        
        xlen1 = len(s1)
        ylen2 = len(s2)
        if(xlen1 + ylen2 != len(s3)):
            return False
        dp = [[False]*(xlen1 + 1) for y in range(ylen2 + 1)]
        dp[0][0] = True
        for y in range(1,ylen2+1):
            if dp[y-1][0] == True:
                dp[y][0] = (s3[y-1] == s2[y-1])
            else:
                break
        for x in range(1,xlen1+1):
            if dp[0][x-1] == True:
                dp[0][x] = (s3[x-1] == s1[x-1])
            else:
                break
        
        for y in range(1,ylen2+1):
            for x in range(1,xlen1+1):
                dpy = dp[y-1][x]
                dpx = dp[y][x-1]
                if  dpy == False and  dpx== False:
                    dp[y][x] = False
                else:
                    s3v = s3[y+x-1]
                    dp[y][x] = (s2[y-1] == s3v and dpy == True) or (s1[x-1] == s3v and dpx == True)
        return dp[ylen2][xlen1]
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
