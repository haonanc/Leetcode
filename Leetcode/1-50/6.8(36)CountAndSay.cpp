class Solution {
public:
    string countAndSay(int n) {
        return recursion("1",n);
        
    }
    string recursion(string str, int a){
        if(a == 1) return str;
        string ret = "";
        int index = 0;
        int count = 1;
        while(true){
            if(index >= str.length()-1) break;
            if(str.substr(index+1,1) == str.substr(index,1)){
                count ++;    
            }
            else{
                ret = ret + to_string(count) + str.substr(index,1);
                count = 1;
            }
            index ++;
        }
        ret = ret + to_string(count) + str.substr(index,1);     
        return recursion(ret,a-1);
    }
};
