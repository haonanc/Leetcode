class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if(nums.size() < 3) return {};
        int distance = INT_MAX;
        int value;
        sort(nums.begin(),nums.end());
        int a = 0;
        int b;
        int c;
        while(a<nums.size()-2){
            int b = a + 1,c = nums.size() -1;
            int va = nums[a];
            while(b<c){
                int vb = nums[b], vc = nums[c];
                int sum = va + vb + vc;
                int temp;
                temp = sum-target;
                if(temp == 0) return sum;
                if( abs(temp) < distance){
                    distance = abs(temp);
                    value = sum;
                }
                if(temp >= 0) while(nums[c] == vc && c > b)c--;
                if(temp <= 0) while(nums[b] == vb && c > b)b++;
            }
            while(nums[a] == va  && a < nums.size() -2){
                a++;   
        }     
        
        
            }
        return value;  
            
            
        }
        
        
    };
