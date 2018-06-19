class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int digit = 1;
        while(true){
            if(digits[digits.size() - digit] == 9){
                digits[digits.size() - digit] = 0;
                digit++;
                if(digit > digits.size()){
                    digits.insert(digits.begin(),1);
                    break;
                }
                continue;   
            }   
            
            digits[digits.size() - digit] ++; 
            break;
            
        }
        
        
        return digits;
        
    }
};
