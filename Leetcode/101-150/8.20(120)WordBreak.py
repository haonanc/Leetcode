class Solution(object):
    def wordBreak(self, s, wordDict):
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True
        for i in range(1,l+1):
            for p in range(i,l+1):
                # print(p,i,s[i-1:p])
                if dp[i-1] == True and s[i-1:p] in wordDict:
                    dp[p] = True
        return dp[l]
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
