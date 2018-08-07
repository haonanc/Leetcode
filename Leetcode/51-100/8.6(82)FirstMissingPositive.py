class Solution:
    def firstMissingPositive(self, nums):
        l = len(nums)
        for i in range(l):
            while nums[i] < l and nums[i] > 0:
                if nums[i] == nums[nums[i]-1]:
                    break
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        print(nums)
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1
                
                
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
