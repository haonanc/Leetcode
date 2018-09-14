class Solution:
    def wordBreak(self, s, wordDict):
        
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True
        for i in range(1,l+1):
            for p in range(i,l+1):
                # print(p,i,s[i-1:p])
                if dp[i-1] == True and s[i-1:p] in wordDict:
                    dp[p] = True
        if dp[-1] == False:     
            return []

        dp = [[] for _ in range(len(s)+1)]
        dp[0].append("")
        for x in range(len(s)):
            for y in range(x+1,len(s)+1):
                if s[x:y] in wordDict and dp[x] != []:
                    if y == len(s):
                        space = ""
                    else:
                        space = " "
                    
                    if dp[x][0] == "":
                        dp[y].append(s[x:y] + space)
                    else:
                        for item in dp[x]:
                            dp[y].append(item + s[x:y] + space)
                                
        return dp[-1]
                    
                    
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
