class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        bool  rows[n] = {false};
        bool  columns[n] = {false};
        bool  leftdia[2*n-1] = {false};
        bool  rightdia[2*n-1] = {false};
        vector<vector<string>> ret;
        vector<string> toPush(n,"");
        backtracking(0,0,ret,n,n,toPush, rows,columns,leftdia,rightdia);
        return ret;  
    }
    
    void backtracking(int x, int y, vector<vector<string>>& ret, int n, int left,vector<string> toPush,bool rows[],bool columns[], bool leftdia[], bool rightdia[]){
        if(n-y<left) {
            return;
        }
        
        int nx = x;
        int ny = y;
        if(nx == n -1){
            nx = 0;
            ny ++;
        }
        else nx ++;
        if(ny == n){
             if(rows[x] == false && columns[y] == false && leftdia[x+y] == false && rightdia[x-y+n-1] == false && left == 1){
                 toPush[y] = toPush[y] + "Q";
                 ret.push_back(toPush);
                 return;
             }
             if(left == 0){
                 toPush[y] = toPush[y] + ".";
                 ret.push_back(toPush);
                 return;
             }
             return;
                 
            
        }
        cout << x << y ;
        if(rows[x] == false && columns[y] == false && leftdia[x+y] == false && rightdia[x-y+n-1] == false ){
            
            rows[x] = true; 
            columns[y] = true;
            leftdia[x+y] = true;
            rightdia[x-y+n-1] = true;
            toPush[y] = toPush[y] + "Q";
            backtracking(nx,ny,ret,n,left-1,toPush,rows,columns,leftdia,rightdia);
            toPush[y].pop_back();
            rows[x] = false; 
            columns[y] = false;
            leftdia[x+y] = false;
            rightdia[x-y+n-1] = false; 
            cout << "5";
        }
        toPush[y] = toPush[y] + ".";
        backtracking(nx,ny,ret,n,left,toPush,rows,columns,leftdia,rightdia);
        toPush[y].pop_back();
    }
};
