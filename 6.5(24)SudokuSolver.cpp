class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        bool columns[9][9] = {false};
        bool rows[9][9] = {false};
        bool grids[9][9] = {false};
        for(int x = 0; x < 9; x++){
            for(int y = 0; y < 9; y++){
                if(board[y][x] != '.'){
                    
                    columns[x][int(board[y][x])-49] = true;
                    rows[y][int(board[y][x])-49] = true;
                    grids[(y/3)*3+x/3][int(board[y][x])-49] = true; 
                }
            }
        }
        int ny = 0;
        int nx = 0;
        
        while(board[ny][nx] !='.'){
                if(nx == 8 && ny != 8){
                    nx = 0;
                    ny++;
                }
                else nx++;
            }    
        backtrace(board,nx,ny,rows,columns,grids);
        
        
    }
    
    bool backtrace(vector<vector<char>>& board, int x, int y, bool rows[9][9],bool columns[9][9],bool grids[9][9]){
        
        
        
        int give = 1;
        while(give < 10){
            
            
            if(rows[y][give-1] == false && columns[x][give-1] == false && grids[(y/3)*3+x/3][give-1] == false){
            if(x == 6&& y == 8) cout << "max" <<give;

            rows[y][give-1] = true;
            columns[x][give-1] = true;
            grids[(y/3)*3+x/3][give-1] = true;
            board[y][x] = give + '0'; 
            
            int nx = x + 1;
            int ny = y;
            if(nx == 9) {
                ny ++;
                nx = 0;
            }
            if(ny ==9) return true;
                
            
                
            
            while(board[ny][nx] !='.'){
                if(nx == 8){
                    nx = 0;
                    ny++;
                    if(ny == 9) {
                board[y][x] = give + '0';
                return true;    
                        }
                }
                else nx++;
            }      
            
                
            if(backtrace(board,nx,ny,rows,columns,grids) == false){
                rows[y][give-1] = false;
                columns[x][give-1] = false;
                grids[(y/3)*3+x/3][give-1] = false;
                give ++;
            }
            else{
                board[y][x] = give + '0';
                return true;
            }
        }
        else{
            give++;
        }
            
        }
        // cout << "invalid" << x << y;
        board[y][x] = '.';
        return false;      
        
    }
};
