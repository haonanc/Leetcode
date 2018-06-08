class Solution {
public:
    string longestPalindrome(string s) {
        string longest = "";
        int index = 0;
        int max = s.length();
        int len = s.length();
        while(max!=0){
            if(test(s.substr(index,max))){
        return(s.substr(index,max));
            }
            if(index + max == len){
                index = 0;
                max --;
            }
            else{
                index++;
            }
            
        }
        string re = "";
        return re;
        
    }
    
    bool test(string str){
        string o = str;
        int n = o.length();

    for (int i=0; i<n/2; i++){
        swap(o[i], o[n-i-1]);
    }
    
    if(o == str){
        return true;
    }
    return false;

    
}
};
