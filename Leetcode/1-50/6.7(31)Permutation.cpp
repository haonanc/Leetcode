class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ret;
        vector<int> v;
        recursion(v,ret,nums);
        return ret;
        
        
        
    }
    
    void recursion(vector<int> v,vector<vector<int>>& ret,vector<int> left){
        if(left.size() == 0) ret.push_back(v);
        for(int a = 0; a < left.size(); a++){
            v.push_back(left[a]);
            int temp = left[a];
            left.erase(left.begin()+a);
            recursion(v,ret,left);
            v.pop_back();
            left.insert(left.begin()+a,temp);
        }
        
        
        
    }
};
