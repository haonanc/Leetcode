class Solution:
    def canCompleteCircuit(self, gas, cost):
        s = 0
        helper = [0]*len(cost)
        for i in range(len(cost)):
            s += ( gas[i] - cost[i])
        if s < 0:
            return -1
        balance = 0
        p = 0
        for i in range(len(cost)):
            balance += (gas[i] - cost[i])
            if balance < 0:
                balance = 0
                p = i + 1
        return p
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
