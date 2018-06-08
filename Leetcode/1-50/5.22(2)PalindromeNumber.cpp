class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int r = reverse(x);
            if(x == r){
                return true;
            }
            return false;
        
    }
    
    int reverse(int x ){
        int total = 0;
        while(x){
            total = total*10 + x%10;
            x = x/10;
        }
        return total;
    }
};
