class Solution:
    def longestConsecutive(self, nums):      
        d = {}
        m = -1
        for i in nums:
            if i in d:
                continue
            if i+1 in d and i-1 in d:
                d[i] = None
                temp = [d[i-1][0],d[i+1][1]]
                m = max(m,abs(d[i+1][1]-d[i-1][0]))
                d[d[i-1][0]] = temp
                d[d[i+1][1]] = temp       
            elif i+1 in d:
                d[i] = d[i+1]
                d[i][0] = i
                m = max(m,abs(d[i][1]-d[i][0]))
            elif i-1 in d:
                d[i] = d[i-1]
                d[i][1] = i     
                m = max(m,abs(d[i][1]-d[i][0]))
            else:
                d[i] = [i,i]
                m = max(m,0)
        return m+1
                
            
            
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
