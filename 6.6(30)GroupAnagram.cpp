#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //97 a;
        
        int dic[strs.size()][26] = {0};
        
        vector<vector<string>> ret;
        int fin = 0;
        
        
        for(int a =0; a<strs.size(); a++){
            //create an array for comparision
            int com[26] = {0};
            for(int b = 0; b < strs[a].length(); b++){
                com[strs[a].at(b) - 97] ++;
            }
            
            int temp = 0;
            bool found = false;
            while(temp < fin){
                if (equal(begin(com), end(com), begin(dic[temp]))){
                    ret[temp].push_back(strs[a]);
                    cout << strs[a];
                    found = true;
                    break;
                }
                temp ++;
            }
            if(found) continue;
             
            vector<string> toPush;
            toPush.push_back(strs[a]);
            ret.push_back(toPush);
            copy(begin(com), end(com), begin(dic[fin]));
            fin++;
    
        }
        return ret;
        
        
    }
};
