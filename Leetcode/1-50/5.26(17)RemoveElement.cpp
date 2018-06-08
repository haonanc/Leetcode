class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int x= 0;
        while(x< nums.size()){
            if(nums[x] == val) nums.erase(nums.begin()+x);
            else x++;
        }
        return nums.size();
        
    }
};
