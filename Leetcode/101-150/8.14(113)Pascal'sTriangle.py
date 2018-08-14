class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        toRet = [[1,1] for y in range(1,numRows+1)]
        del toRet[0][0]
        
        for i in range(2,max(2,numRows)):
            temp = toRet[i]
            pre = toRet[i-1]
            for p in range(1,i):
                temp.insert(p,pre[p-1]+pre[p])
        
        return toRet
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
