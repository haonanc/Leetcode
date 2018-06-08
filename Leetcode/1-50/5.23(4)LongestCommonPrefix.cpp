class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0){
            string empty = "";
            return empty;
        }
        string prefix = strs[0];
        for(string str: strs){
            int index = 0;
            while(index < prefix.length()){
                if(index == str.length()){
                    prefix = str ;
                    break;
                }
                
                if(str.at(index) != prefix.at(index)){
                    prefix = str.substr(0,index);
                    break;
                }
                
                index ++;
            }
            
        }
        return prefix;
        
    }
};
