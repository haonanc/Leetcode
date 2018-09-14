class Solution(object):
    def trailingZeroes(self, n):
        ret = 0
        a = 5
        while(n>=a):
            ret += n//a
            a *= 5
        return ret
        """
        :type n: int
        :rtype: int
        """
        
