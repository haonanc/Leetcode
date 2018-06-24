class Solution:

        

            
            
    def binarySearch(self,nums,target,left,right):
        while right >= left:
            m = int((left + right) / 2)
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return left,m,right
        return -1,-1,-1
    
    def binarySearchLeft(self,nums,target,left,right,ret):
        while right >= left:
            
            m = int((left + right) / 2)
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                ret[0] = m
                self.binarySearchLeft(nums,target,left,m-1,ret)
                break
    
    def binarySearchRight(self,nums,target,left,right,ret):
        while right >= left:
            m = int((left + right) / 2)
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                ret[1] = m
                self.binarySearchRight(nums,target,m+1,right,ret)
                break
                
    def searchRange(self, nums, target):
        left,mid,right = self.binarySearch(nums,target,0,len(nums) - 1) 
        if left == -1:
            return [-1,-1]
        ret = [mid,mid]
        self.binarySearchLeft(nums,target,left,mid-1,ret)
        self.binarySearchRight(nums,target,mid+1,right,ret)
        return ret
    
        
        
        
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
