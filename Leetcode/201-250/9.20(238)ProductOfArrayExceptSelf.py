class Solution:
    def productExceptSelf(self, nums):
        if nums == []:
            return []
        ret = []
        recursion(nums,1,0,ret)
        return ret
        """
        :type nums: List[int]
        :rtype: List[int]
        """

def recursion(nums,pre,index,ret):
    if index != len(nums) -1:
        post = recursion(nums,pre*nums[index],index+1,ret)
    else:
        post = 1   
    ret.insert(0,pre*post) 
    return post*nums[index]
