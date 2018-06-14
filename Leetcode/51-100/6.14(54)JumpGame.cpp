class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size() == 0) return false;
        if(nums.size() == 1) return true;
        int cur = nums[0];
        int max = cur;
        int index = 0;
        int maxindex = 0;
        
        while(true){
            for(int a = 1;a <= cur; a++){
                int c = a+nums[index + a];
            if(c > max){
                max = c;
                maxindex = index + a;
            }
        }
            
        index = maxindex;
        maxindex = index + 1; 
        cur = nums[index];
        max = cur;
        if(cur == 0) return false;
        if(cur + index >=nums.size()-1) return true;


            
        }
        
        
            
    }
};
