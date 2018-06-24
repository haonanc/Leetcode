class Solution:
    def multiply(self, num1, num2):
        
        if(num1 == "0" or num2 == '0'):
            return "0"
        
        s1 = len(num1) - 1
        s2 = len(num2) - 1
        ret= [0]*220
        
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        for a in range(0,len(num2)):
            for b in range(0,len(num1)):
                ret[219-a-b] += int(num2[s2 - a])*int(num1[s1 - b])
        
        
        

        for i in range(0,220):
            temp = ret[219-i]
            dex = 1
            ret[219-i] = temp % 10 
            temp = temp //10
            while(temp > 0):
                print(temp)
                temp2 = temp % 10
                temp = temp //10
                ret[219-i-dex] += temp2
                dex += 1
            
        ind = next((i for i, x in enumerate(ret) if x), None)    
        ret = ret[ind:]
        toRet = ""   
        for item in ret:
            toRet += str(item)
        return toRet
            
            
            
