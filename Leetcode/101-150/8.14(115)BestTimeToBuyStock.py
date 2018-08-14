class Solution(object):
    def maxProfit(self, prices):
        am,m = 0,0
        for i in range(1,len(prices)):
            m = max(0,m+prices[i]-prices[i-1])
            am = max(am,m)
        return am
        """
        :type prices: List[int]
        :rtype: int
        """
        
