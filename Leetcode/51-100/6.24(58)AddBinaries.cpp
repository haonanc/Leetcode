class Solution {
public:
    string addBinary(string a, string b) {
        
        int am = a.length();
        int bm = b.length();
        string ret;
        int retm;
        if(am > bm){
            retm = a.length();
            ret = a;
        }
        else {
            retm = b.length();
            ret = b;
        }
        
        int m = min(am,bm);
        int index = 0;
        int next = 0;
        while(index < m){
            char c = a[am - index-1] + b[bm - index-1] + next;
            if(c == 97) {
                next = 0;
                ret[retm - index-1] = '1';
            }
            else if(c == 98) {
                ret[retm -index-1] = '0';
                next = 1;
            }
            else if(c == 99){
                next = 1;
                ret[retm -index - 1] = '1';
            }
            else next = 0;
        index ++;
        }
        if(next == 1){
             while(index < ret.length()){
                 if(ret[retm - index-1] =='0'){
                     ret[retm - index-1] ='1';
                     next = 0;
                     break;
                 }
                 ret[retm - index-1] ='0';
                 index++;
        }
        if(next == 1){
            ret.insert(0,"1");

        }
            
        }
       
        return ret;
        
        
    }
};
