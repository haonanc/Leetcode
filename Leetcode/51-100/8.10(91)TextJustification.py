class Solution:
    def fullJustify(self, words, maxWidth):
        if len(words) == 0:
            return []
        end,start = 0,0
        toRet = []
        
        left = maxWidth
        
        while end < len(words):
            if(len(words[end])) <= left:
                left -= (len(words[end])+1)
                end += 1
            else:
                temp =""      
                counter = 0
                left += (end - start) 
                for word in words[start:end]: 
                    length = int(math.ceil(left/max(end - start-1-counter,1)))
                    temp += word + " "*min(length,left)
                    counter += 1
                    left -= length
                toRet.append(temp)
                start = end
                left = maxWidth
        temp = ""
        left += (end - start) 
        for word in words[start:end]: 
            temp += word + " "*min(1,left)
            left -= 1
        temp += " "*left
        toRet.append(temp)
        return toRet

            
            
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
