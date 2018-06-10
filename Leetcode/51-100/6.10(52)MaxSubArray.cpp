int x=[](){
   std::ios::sync_with_stdio(false);  
    cin.tie(NULL);
    return 0;
}();


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int sum = 0;
        int largest = nums[0];
        for(int i = 0; i <nums.size(); i++){
            if(nums[i]+sum < 0){
                sum = 0;
                largest = max(largest,nums[i]);
            }
            else{
                 sum += nums[i]; 
                largest = max(largest,sum); 
            } 
        }      
        return largest;
        
        
    }
};
