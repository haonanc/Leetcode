class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int low = 0;
        int length = matrix.size();
        int border = matrix.size()-1;
        int iter = 0;
        int helper = 0;
        
        if(matrix.size()%2 == 0) low = 0;
        else low  = 1;
        while(length !=low){
                helper = 0;
                while(helper<length-1){
                
                int a = matrix[iter][iter+helper];
                int b = matrix[iter+helper][border- iter];//matrix[y][x]
                int c = matrix[border - iter][border- iter-helper];
                int d = matrix[border- iter-helper][iter];
                matrix[iter+helper][border- iter] =a;
                matrix[border - iter][border- iter-helper]=b;
                matrix[border- iter-helper][iter]= c;
                matrix[iter][iter+helper] = d;
                helper ++;
                }             
                iter ++;
                length = length -2;
            
            
            
        }
        
    }
};
