class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        m = nums[0]
        h,l = 1,1
        
        for i in nums:
            if i == 0:
                h, l =  1, 1
                m = max(0,m)
                continue
            h,l = max(l*i,h*i,i),min(l*i,h*i,i)
            m = max(m,h)
            print(h,l)
        return m
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
