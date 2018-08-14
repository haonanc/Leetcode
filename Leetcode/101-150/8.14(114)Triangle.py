class Solution(object):
    def minimumTotal(self, triangle):
        height = len(triangle)
        if height == 0:
            return 0
        for level in range(1,height):
            temp = triangle[level]
            pre = triangle[level-1]
            for index in range(0,level+1):
                if index == 0:
                    temp[index] += pre[0]
                elif index == level:
                    temp[index] += pre[level-1]
                else:
                    temp[index] += min(pre[index],pre[index-1])
                    
            
        
        return min(triangle[height-1])
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
