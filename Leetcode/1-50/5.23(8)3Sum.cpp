class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> re;
        if(nums.size()<3){
            return re;
        }
        int a = 0;
        int b;
        int c;
        int ta;
        int tb;
        int tc;
        int sum;
        sort(nums.begin(),nums.end());
        while(a < nums.size() -1){
            b = a + 1;
            c = nums.size() - 1;
            int va = nums[a];
            while(c>b){
                tb = b + 1;
                tc = c - 1;
                int vb =nums[b], vc =nums[c];
                
                sum = va+vb+vc;
                
            if(sum == 0) re.push_back({va,vb,vc});
            if(sum >=0) {
                while(nums[tc] == vc&& tc > b)tc--;
                c = tc;}
                
            if(sum <=0) {
                while(nums[tb] == vb&& c > tb)tb++;
                b = tb;}
            } 
            ta = a + 1;
            while(nums[ta] == va  && ta < nums.size() -1){
                ta++;   
        }     
            a = ta;
            }
        
        return re;
        
    }
};
