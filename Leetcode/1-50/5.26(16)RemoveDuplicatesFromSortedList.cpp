class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int x = 1;
        int dup = nums[0];
        int distinct = 1;
        while(x<nums.size()){
            
            if(nums[x] == dup) x++;
            else{
                nums[distinct] = nums[x];
                dup = nums[x];
                distinct ++;
                x++;
                }
            
        }
        return distinct;
        
    }
};
