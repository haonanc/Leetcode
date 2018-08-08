class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        cur = "0"*(n)
        toRet = [0]
        store = ['0']
        for i in range(n-1):
            store.append(str(i+1)+" "+" ".join(store))
        iter = " ".join(store).split(" ")
        for i in range(len(iter)):
            temp = n - (int(iter[i])+ 1)
            if cur[temp] == "0":
                cur = cur[:temp] + '1' + cur[temp+1:]
            else:
                cur = cur[:temp] + '0' + cur[temp+1:]
            toRet.append(int(cur,2))
            
        return toRet 
        """
        :type n: int
        :rtype: List[int]
        """
        
