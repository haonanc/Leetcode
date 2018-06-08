class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int begin = 0;
        int end = 0;
        int longest = 0;
        int temp = 0;
        int length = s.length();
        map<string,int> m;
        while(end<length){
            string str = s.substr(end,1);
            if ( m.find(str) == m.end() ){
                m[str] = end;
                end++;
                temp ++;; 
            }
            else{
                if(temp > longest) longest = temp;
                begin = m[str] + 1;
                end = begin;
                temp = 0;  
                m.clear();
            }         
        }
        if(temp > longest) longest = temp;
        return longest;     
    }
};
