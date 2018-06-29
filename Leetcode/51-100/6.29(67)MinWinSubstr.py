class Solution:
    def minWindow(self, s, t):
        check = {}
        helper = []
        m = 0
        left = len(t)
        toRet = []
        found = False
        for i in range(0,len(t)):
            if(t[i] not in check):
                check[t[i]] = [-1]
            else:
                check[t[i]].append(-1)
        # check[s[i]] the list
        for i in range(0,len(s)):
            if(s[i] in check):
                minIndex = min(check[s[i]])
                if(minIndex == -1):
                    left -= 1 
                    helper.append(i)
                    if(left == 0):
                        check[s[i]][check[s[i]].index(minIndex)] = i 
                        found = True
                        m = max(helper) - min(helper) + 1
                        toRet = [min(helper),max(helper)]
                        continue
                check[s[i]][check[s[i]].index(minIndex)] = i  
                if(minIndex != -1):
                    helper[helper.index(minIndex)] = i
                if(found):

                    temp = max(helper) - min(helper) + 1
                    if(temp < m):
                        print("smaller value",m,temp)
                        m = temp
                        toRet = [min(helper),max(helper)] 
        if(left != 0):
            return ""
        return s[toRet[0]:toRet[1]+1]
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
