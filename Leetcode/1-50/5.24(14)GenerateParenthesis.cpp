class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> list;
        if(n == 0) return list;
        recursion(n,0,list,"");
        return list;
        
        
    }
    
    void recursion(int left, int st, vector<string>& list, string str){
        if(left == 0 && st == 0) {
            list.push_back(str);
            return; //base case
        }
        else if(left != 0){
            if(st == 0){
                recursion(left-1,1,list,str+"(");
            }
            else{
                recursion(left, st - 1,list,str+")");
                recursion(left-1, st + 1,list,str+"(");
            }
        }
        else{
             recursion(left, st -1,list,str+")");
            
            
        }
        
    }
};
