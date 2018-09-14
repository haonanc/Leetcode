class Solution(object):
    def rotate(self, nums, k):
        r = len(nums) - k % len(nums)
        nums[:] = nums[r:]+nums[:r]
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
