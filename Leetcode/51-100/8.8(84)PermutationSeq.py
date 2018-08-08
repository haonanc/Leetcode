class Solution:
    def getPermutation(self, n, k):
        k = k - 1
        list = [0]
        left = []
        toRet = ""
        temp = 1
        for i in range(1,n+1):
            temp *= i
            left.append(str(i))
            list.append(temp)

        while(n!=1):
            s = left[k // list[n-1]]
            toRet += s
            left.remove(s)
            k = k % list[n-1]
            n -= 1
        return toRet+left[0]
            
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
