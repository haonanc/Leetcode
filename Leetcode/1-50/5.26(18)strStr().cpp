class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle == "") return 0;
        int index = 0;
        int plus = 0;
        while(index < haystack.length()){
            while(haystack[index+plus] == needle[plus]){
                if(plus + 1<needle.length()){
                    if(plus + index >= haystack.length()) break;
                    else plus ++;
                }
                else return index;
            }
    
            index ++;
            plus = 0;
            
        }
        return -1;
        
        
        
    }
};
