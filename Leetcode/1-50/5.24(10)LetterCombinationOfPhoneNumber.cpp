class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
        vector<string> v;
        if(digits == "") return v;
        recursion(digits,"",v);
        return v;
        
    }
    
    void recursion(string digits, string toPush, vector<string>& v){
        int s = digits.size() - 1;
        if(digits == ""){
            v.push_back(toPush);
            return;
        }
        
        if(digits.substr(0,1) == "2"){
            recursion(digits.substr(1,s),toPush+"a",v);
            recursion(digits.substr(1,s),toPush+"b",v);
            recursion(digits.substr(1,s),toPush+"c",v);
            return;
        }
        
        if(digits.substr(0,1) == "3"){
            recursion(digits.substr(1,s),toPush+"d",v);
            recursion(digits.substr(1,s),toPush+"e",v);
            recursion(digits.substr(1,s),toPush+"f",v);
            return;
        }
        
        if(digits.substr(0,1) == "4"){
            recursion(digits.substr(1,s),toPush+"g",v);
            recursion(digits.substr(1,s),toPush+"h",v);
            recursion(digits.substr(1,s),toPush+"i",v);
            return;
        }
        
        if(digits.substr(0,1) == "5"){
            recursion(digits.substr(1,s),toPush+"j",v);
            recursion(digits.substr(1,s),toPush+"k",v);
            recursion(digits.substr(1,s),toPush+"l",v);
            return;
        }
        
         if(digits.substr(0,1) == "6"){
            recursion(digits.substr(1,s),toPush+"m",v);
            recursion(digits.substr(1,s),toPush+"n",v);
            recursion(digits.substr(1,s),toPush+"o",v);
            return;
        }
        
        if(digits.substr(0,1) == "7"){
            recursion(digits.substr(1,s),toPush+"p",v);
            recursion(digits.substr(1,s),toPush+"q",v);
            recursion(digits.substr(1,s),toPush+"r",v);
             recursion(digits.substr(1,s),toPush+"s",v);
            return;
        }
        
        if(digits.substr(0,1) == "8"){
            recursion(digits.substr(1,s),toPush+"t",v);
            recursion(digits.substr(1,s),toPush+"u",v);
            recursion(digits.substr(1,s),toPush+"v",v);
            return;
        }
        
        if(digits.substr(0,1) == "9"){
            recursion(digits.substr(1,s),toPush+"w",v);
            recursion(digits.substr(1,s),toPush+"x",v);
            recursion(digits.substr(1,s),toPush+"y",v);
            recursion(digits.substr(1,s),toPush+"z",v);
            return;
        }
        
        
    }
};
