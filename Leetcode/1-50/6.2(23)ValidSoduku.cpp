class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> columns(9);
        vector<set<char>> rows(9);
        vector<set<char>> grids(9);
        
        for(int a = 0; a < 9; a++){
            for(int b= 0;b < 9;b++){
                char c = board[a][b];
                if(c != '.'){
                    if((rows[b]).count(c) == 1) return false;
                   if((columns[a]).count(c) == 1) return false;
                
                   rows[b].insert(c);
                   columns[a].insert(c);
                
                   int x = (a/3)*3  + (b/3);
                   if((grids[x]).count(c) == 1) return false;
                   grids[x].insert(c);    
                }
                
            }
            
        }
        return true;
        
        
    }
};
