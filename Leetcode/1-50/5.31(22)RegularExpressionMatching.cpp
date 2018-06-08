class Solution {
public:
    bool isMatch(string s, string p) {
        bool ret = false;
        if(s == ""){
            if(p == "" ) return true;
            else if(p.length() > 1?p.substr(1,1) == "*":false) star(s,p,ret);
            else return false;
        }   
        if(p.length() > 1?p.substr(1,1) == "*":false) star(s,p,ret);
        else recursion(s,p,ret);
        
        return ret;
        
    }
    
    void recursion(string s,string p, bool& ret){
        if(s =="") return;
        if((p.substr(0,1) == s.substr(0,1))|| p.substr(0,1) == "."){
            if(s.length() == 1){
                if(p.length() == 1) {
                    ret = true;
                    return;
                }
           }
            if(p.length() == 1) return;
            
            p = p.substr(1,p.length()-1);//modification 
            if(s.length() >1)s = s.substr(1,s.length()-1);
            else s = "";
            
            if(p.length() > 1?p.substr(1,1) == "*":false) star(s,p,ret);
            else recursion(s,p,ret);
        }
}
    
    void star(string s,string p, bool& ret){
        if(s ==""){
            if(p.length() ==2) ret = true;
            else{
                p = p.substr(2,p.length()-2);
                if(p.length() > 1?p.substr(1,1) == "*":false) star(s,p,ret);  
            }
            return;  
        }
        
        string s2 = s;
        string p2 = p;
        //case 1; star = 0;
        if(p.length() != 2){
            p = p.substr(2,p.length()-2);
            if(p.length() > 1?p.substr(1,1) == "*":false) star(s,p,ret);
            else recursion(s,p,ret);      
        }
        
        //case 2; star continues

        if((p2.substr(0,1) ==s2.substr(0,1))||p2.substr(0,1) == "."){
            if(s2.length() == 1) star("",p2,ret);
            else star(s2.substr(1,s2.length()-1),p2,ret);
        }
        
        
}
};
