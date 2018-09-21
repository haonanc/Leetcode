class Solution:
    def majorityElement(self, nums):
        count = 1
        ret = nums[0]
        for i in range(1,len(nums)):
            if ret == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    ret = nums[i]
                    count = 1


                    
        
        
        return ret
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
