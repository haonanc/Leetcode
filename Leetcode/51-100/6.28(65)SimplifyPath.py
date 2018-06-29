class Solution:
    def simplifyPath(self, path):
        pointer = 0
        path += "/"
        store = [""]
        tempstr = ""
        
        while(path!=""):
            temp = path[0]
            path = path[1:]
            if(temp == "/"):
                if(tempstr == ""):
                    continue
                else:
                    if(tempstr == "."):
                        tempstr = ""
                    elif(tempstr == ".."):
                        tempstr = ""
                        if(pointer != 0):
                            pointer -=1
                    else:
                        if(len(store) <= pointer):
                            store.append("")
                        store[pointer] = tempstr
                        pointer +=1
                        tempstr = ""                 
            else:
                tempstr += temp
        if(len(store) <= pointer):
            store.append("")
        store[pointer] = tempstr
        toRet = "/"+'/'.join(store[:pointer+1]).strip("/")
        return toRet
        
        """
        :type path: str
        :rtype: str
        """
        
