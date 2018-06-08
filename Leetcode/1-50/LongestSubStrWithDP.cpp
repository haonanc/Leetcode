class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0) return 0;
        vector<int> v(256,-1);
        int len = 0, begin = -1;
        for(int i = 0; i < s.length(); i ++){
            if(v[s[i]] > begin){
                begin = v[s[i]];               
            }
            v[s[i]] = i;
            len = max(len,i - begin);
        }
        return len;
        
    }
};
