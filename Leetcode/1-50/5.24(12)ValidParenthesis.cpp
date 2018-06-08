#include<stack>
class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        for(int i = 0; i < s.length(); i++){
            if(s.substr(i,1) == "(") st.push(1);
            else if(s.substr(i,1) == "[") st.push(2);
            else if(s.substr(i,1) == "{") st.push(3);
            else if(st.empty()) return false;
            else if(s.substr(i,1) == ")") {
                if(st.top() == 1){
                    st.pop();
                }
                else{
                    return false;
                }
            }
            else if(s.substr(i,1) == "]") {
                if(st.top() == 2){
                    st.pop();
                }
                else{
                    return false;
                }
            }
            else if(s.substr(i,1) == "}") {
                if(st.top() == 3){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        if(!st.empty()) return false;
        return true;
        
    }
};
