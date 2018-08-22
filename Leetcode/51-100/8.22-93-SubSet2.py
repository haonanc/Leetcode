class Solution:
    def subsetsWithDup(self, nums):
        if nums == []:
            return nums
        ret = [[]]
        list.sort(nums)
        recursion(nums,ret,0,len(nums)-1,0,-2**31)
        return ret
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
def recursion(nums,toRet,count,m,l,h):
    cur = nums[count]
    if cur == h:
        for i in range(len(toRet)-l,len(toRet)):
            temp = copy.deepcopy(toRet[i])
            temp.append(cur)
            toRet.append(temp)
    else:  
        l = len(toRet)
        for i in range(l):
            temp = copy.deepcopy(toRet[i])
            temp.append(cur)
            toRet.append(temp)   
    if count < m:
        recursion(nums,toRet,count+1,m,l,cur)
        
    
    
