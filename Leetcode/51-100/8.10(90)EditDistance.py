class Solution:
    def minDistance(self, word1, word2):
        l_word1 = len(word1)
        l_word2 = len(word2)
        if l_word1 == 0 or l_word2 == 0:
            return max(l_word1,l_word2)
        dp = [[-1]* (l_word1 + 1) for x in range(l_word2+1)]
        dp[0][0] = 0 
        for x in range(1,l_word1+1):
            dp[0][x] = x
        for y in range(1,l_word2+1):
            dp[y][0] = y
        for x in range(1,l_word1+1):
            for y in range(1,l_word2+1):
                if word1[x-1] == word2[y-1]:
                    dp[y][x] = dp[y-1][x-1]
                else:
                    dp[y][x] = min(dp[y-1][x]+1,dp[y][x-1]+1,dp[y-1][x-1]+1)
        return dp[y][x]
                
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
