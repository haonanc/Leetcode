class Solution {
public:
    int reverse(int x) {
        long total = 0;
        while(x){
            total = total * 10 + x%10;
            x = x/10;
        }
        return (total > INT_MAX || total<INT_MIN) ? 0:total;
        
    }
};
