class Solution {
public:
    string intToRoman(int num) {
        int x = num%10;
        int y = (num/10)%10;
        int z = (num/100)%10;
        int t =  num/1000;
        string ret = "";
        
        for(int i = 0; i < t; i++) ret = ret + "M";
        
        if(z == 4) ret = ret + "CD";
        else if(z == 9) ret = ret + "CM";
        else if(z >4) {
            ret = ret + "D";
            for(int i = 0; i < z - 5; i++) ret = ret + "C";
        }
        else for(int i = 0; i < z; i++) ret = ret + "C";
        
        if(y == 4) ret = ret + "XL";
        else if(y == 9) ret = ret + "XC";
        else if(y >4) {
            ret = ret + "L";
            for(int i = 0; i < y - 5; i++) ret = ret + "X";
        }
        else for(int i = 0; i < y; i++) ret = ret + "X";
        
        if(x == 4) ret = ret + "IV";
        else if(x == 9) ret = ret + "IX";
        else if(x >4) {
            ret = ret + "V";
            for(int i = 0; i < x - 5; i++) ret = ret + "I";
        }
        else for(int i = 0; i < x; i++) ret = ret + "I";
        
        return ret;
        
        
        
        
    }
};
