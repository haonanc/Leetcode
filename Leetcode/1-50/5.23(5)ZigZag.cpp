#include<vector>
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows >= s.length()){
            return s;
        }
        if(numRows == 1){
            return s;
        }
        
        vector<string> rows(numRows, "");// initialize the vector
        int index = 0;
        bool downward = true;
        int height = 0;
        while(index<s.size()){
            rows[height] += s.substr(index,1);
            if(downward == true){
                height++;
            }
            else{
                height--;
            }
            if(height == 0){
                downward = true;
            }
            if(height == numRows -1){
                downward = false;
            }
            index++;
        }
        string strs = "";
        for(string str: rows){
            strs += str;
        }
        return strs;
        
    }
};
