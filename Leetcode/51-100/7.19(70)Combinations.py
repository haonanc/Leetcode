class Solution:
    def combine(self, n, k):
        if(n == 0):
            return []
        toRet = []
        temp = []
        recursion(1,toRet,temp,n,k)
        return toRet
                
def recursion(index,toRet,temp,n,k):
    if(len(temp) == k):
        toRet.append(temp.copy())
        return
    for i in range(index,n+1):
        temp.append(i)
        recursion(i+1,toRet,temp,n,k)
        temp.pop()
                
            
            
            
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
