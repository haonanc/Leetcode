class Solution {
public:
    int romanToInt(string s) {
        int ret = 0;
        map<char,int> m =  {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        for(int a = 0; a < s.length(); a++){
            char x = s[a];
            ret = ret + m[x];
            if(a !=0){
                string temp = s.substr(a-1,2);
                if(temp == "CD" | temp == "CM" |temp == "XL" |temp == "XC" |temp == "IV"|temp == "IX" ) ret = ret - 2*m[s[a-1]];  
            }           
        } 
        return ret;

        
        
    }
};
