class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int left = 0;
        int right = height.size() - 1;
        int temp;
        while(left!=right){
            if(height[left] > height[right]){
                temp = height[right]*(right-left);
                if(temp > max) max = temp;
                right --;
            }
            else{
                temp = height[left]*(right-left);
                if(temp > max) max = temp;
                left ++;
            }
            
            
        }
        return max;
        
    }
    

};
