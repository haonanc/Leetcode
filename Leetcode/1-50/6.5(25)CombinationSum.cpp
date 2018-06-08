class Solution {
public:
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int>> ret;
        vector<int> toRet;
        int index = 0;
        while(index < candidates.size() ?candidates[index] <=target :false){
            recursion(candidates, target, index, ret, toRet);
            index++;
        }    
        return ret;
    }
    
    void recursion(vector<int>& candidates, int target, int index, vector<vector<int>>& ret, vector<int> toRet){
        target = target - candidates[index];
        toRet.push_back(candidates[index]);
        if(target == 0){
            ret.push_back(toRet);
            return;
        }
        
        while(index < candidates.size() ?candidates[index] <=target :false){
            recursion(candidates, target, index, ret, toRet);
            index++;
        }
        
    }
};
