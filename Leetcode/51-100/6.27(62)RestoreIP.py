class Solution:
    def restoreIpAddresses(self, s):
        
        toRet = []
        self.recursion("",s,toRet,4)
        return toRet
        """
        :type s: str
        :rtype: List[str]
        """
        
    def recursion(self,st,left,toRet,times):
        if(times == 0):
            if(left == ''):
                toRet.append(st[:-1])
                return
            else:
                return
        
        if(len(left)>times*3 or len(left)<times):
            return;
        if(left[0] == "0"):
            self.recursion(st+left[0]+".",left[1:],toRet,times-1)            
        else:
            self.recursion(st+left[0]+".",left[1:],toRet,times-1)
            if(len(left)>1):
                self.recursion(st+left[0:2]+".",left[2:],toRet,times-1)
            if(len(left)>2):
                if(int(left[0:3])<256):
                    self.recursion(st+left[0:3]+".",left[3:],toRet,times-1)
        
        
        
