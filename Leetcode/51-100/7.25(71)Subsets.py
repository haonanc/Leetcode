class Solution:
    def subsets(self, nums):
        toRet = [[]]
        recursion(nums,toRet,0,len(nums)-1)
        return toRet
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
def recursion(nums,toRet,index,max):
    for i in range(len(toRet)):
        newList = copy.copy(toRet[i])
        newList.append(nums[index])
        toRet.append(newList)

    if(index < max):
        recursion(nums,toRet,index+1,max)
    
        
