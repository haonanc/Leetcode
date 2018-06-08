#include <set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max = 1;
        int index = 0;
        int count = 0;
        int iterator = 0;
        set <char> setOfchar = {};
        while(iterator <= s.length()){
            
            if(index == s.length()){
                    if(count > max) max = count;
                    break;
                }
            
            if(setOfchar.count(s.at(index)) == 0){
                setOfchar.insert(s.at(index));
                count ++;   
                
                index ++;
            }
            else{
                setOfchar.empty();
                if(count > max){
                    max = count;
                }
                if(iterator == s.length()) break;
                
                count = 0;
                iterator ++;
                index = iterator;
            }
        }
        return max;
        
        
    }
};
