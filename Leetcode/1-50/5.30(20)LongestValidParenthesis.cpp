#include <stack>
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
        int max = 0;
        if(s.length() == 0) return 0;
        
        for(int i = 0; i < s.length(); i++){
            if(s.substr(i,1) == "(")
                st.push(-1);
            else{
                if(st.empty()) st.push(-2);
                else{
                     int a = st.top();
                     st.pop();
                    if(a == -1){
                        st.push(1);
                        merge(st);
                    }
                    else if((a>0) && (!st.empty())){
                        int b = st.top();
                        st.pop();
                        if(b == -1){
                            st.push(1);
                            st.push(a);
                            merge(st);
                        }
                        else{
                            st.push(b);
                            st.push(a);
                            st.push(-2);
                        }
                    }
                    else{
                        st.push(a);
                        st.push(-2);   
                    }   
                }                
                }
                
                
        }
        while(!st.empty()){
            int c = st.top();
            if(c>max) max = c;
            st.pop();
        }
        return 2*max;
             
    }
    
    void merge(stack<int> & st){
            int b; 
            int a = st.top();
            st.pop();
        if(!st.empty()){
            b = st.top();
            st.pop(); 
        }
        else {
            st.push(a);
            return;
        }        
        if(a > -1 && b > -1){
            st.push(a+b);
            merge(st);
        }
        else {
            st.push(b);
            st.push(a);
        }
    }

};
