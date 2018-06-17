class Solution {
public:
    int lengthOfLastWord(string s) {
        int ret = 0;
        int bo =1;
        for(int i = 0;i<s.size();i++){
            if(s[i] == ' ') bo = 0;
            else {
                cout << bo;
                ret = ret  *bo + 1;
                bo =1;
            }
        }
        
        return ret;
        
    }
};
