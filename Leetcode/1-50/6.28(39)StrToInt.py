class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if(len(s) == 0):
            return 0
        max = 2**31-1
        min = -1*2**31
        i = 1
        toRet = ""

        if(s[0] == "-"):
            s = s[1:]
            i = -1
        elif(s[0] == "+"):
            s = s[1:]
        
        while(s != ""):
            if(s[0].isdigit()):
                toRet += s[0]
                s = s[1:]
            else:
                break
        if(toRet == ""):
            return 0
        else:
            ans = int(toRet) * i
            if(ans > max):
                return max
            elif(ans < min):
                return min 
            return ans
        
        
        
        """
        :type str: str
        :rtype: int
        """
        
