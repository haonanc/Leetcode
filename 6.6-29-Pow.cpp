class Solution {
public:
    double myPow(double x, int n) {
        if(x == 0.0) return 0.0;
        if(x == 1.0) return x;
        if(n == 1) return x;
        if(n == 0) return 1.0;
        
        double ans = 1;
        int temp;
        bool negative = false;
        bool overflow = false;
        if(n < 0)negative = true;
        
        cout << INT_MIN;
        if(n == INT_MIN){
            n = INT_MAX;
            overflow = true;
            temp = x;
        }
        else{
            n = abs(n);
        }
        
        while(true){
            if(n == 0) break;
            if(n% 2 == 1){
                ans = ans * x;
                n --;
            }
            else{
                x = x*x;
                n = n/2;
            }
            
        }
        if(overflow) ans = ans * temp;
        if(negative) return 1/ans;
        return ans;
        
    }
};
