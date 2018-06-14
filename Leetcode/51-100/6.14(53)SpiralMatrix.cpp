class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        cout << "ss";
        int x = 0;
        int y = 0;
        int layer = 0;
        vector<int> ret;
        int ymax = matrix.size();
        if(ymax == 0) return ret;
        int xmax = matrix[0].size();
        if(xmax == 0) return ret;
        bool b = true;

        while(true){            
            while(b){
                ret.push_back(matrix[y][x]);
                if(x + 1 < xmax - layer){
                x++;
            }
                else{  
                    if(y + 1 < ymax - layer){
                        y++;
                        b = false;       
                    }
                    else {
                        return ret;
                    }
                }    
            }
         while(b == false){
                ret.push_back(matrix[y][x]);
                if(y + 1 < ymax - layer){
                y++;
            }
                else{
                    
                    if(x - 1 >=  layer){
                        x--;
                        b = true;       
                    }
                    else return ret;
                }    
            }


         while(b){
                ret.push_back(matrix[y][x]);
                if(x - 1 >=  layer){
                x--;
            }
                else{
                    layer++;
                    if(y - 1 >= layer){
                        y--;
                        b = false;      
                    }
                    else return ret;
                }    
            }
                
        
        while(!b){
                ret.push_back(matrix[y][x]);
                if(y - 1 >= layer){
                    
                y--;
            }
                else{
                    if(x + 1 < xmax - layer){
                        x++;
                        b = true;      
                    }
                    else return ret;
                }    
            }            
        }

        
        
        
        
        
    }
};
