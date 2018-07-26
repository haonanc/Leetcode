class Solution:
    def removeDuplicates(self, nums):
        index = 0
        cur = -29219
        count = 1
        while(index<len(nums)):
            if(cur == nums[index]):
                if(count == 2):
                    del nums[index]
                else:
                    count += 1
                    index +=1
            else:
                count = 1
                cur = nums[index]
                index+=1 
            
            
            
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
