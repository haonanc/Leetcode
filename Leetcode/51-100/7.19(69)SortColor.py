class Solution:
    def sortColors(self, nums):
        if(len(nums)<=1):
            return 
        zero = 0
        one = 0
        two = 0
        for i in range(0,len(nums)):
            if(nums[i] == 0):
                nums.pop(i)
                nums.insert(zero,0)
                zero+=1
                one +=1
                two +=1
            elif(nums[i] == 1):
                nums.pop(i)
                nums.insert(one,1)  
                one +=1
                two +=1
            else:
                nums.pop(i)
                nums.insert(two,2)
                two += 1
                
            
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
