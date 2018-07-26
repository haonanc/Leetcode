class Solution:
    def largestRectangleArea(self, heights):
        if(len(heights) == 0):
            return 0
        interval = [[0,len(heights)-1]]
        new = []
        height = 1
        heightMax = 0
        lowest = 0
        while(len(interval)!=0):
            lowest = 2147483647
            for group in interval:
                begin = group[0]
                for i in range(group[0],group[1]+1):
            
                    if(height > heights[i]):
                        if(i != begin):
                            new.append([begin,i-1])
                            heightMax = max(heightMax,(i-begin)*height)
                        begin = i + 1
                    else:
                        lowest = min(lowest,heights[i])
                if(i >= begin):
                    new.append([begin,i])
                    heightMax = max(heightMax,(i-begin+1)*height)
            interval = new
            height = max(lowest,height+1)
            new = []
                
        return heightMax        
                    
                
                
            
        """
        :type heights: List[int]
        :rtype: int
        """
        
