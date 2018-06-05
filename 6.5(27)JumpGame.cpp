class Solution {
public:
    int jump(vector<int>& nums) {
        int max;
        int pos = 0;
        int size = nums.size();
        
        int times = 0;
        int min = 0;
        int minIn = 0;
        while(pos < size - 1){
            max = nums[pos];
            for(int temp = 1; temp <= max; temp++){
                int temp2 = nums[pos+temp]+temp;
                cout << pos;
                if(temp2 > min){
                    min = temp2;
                    minIn = temp + pos;
                }
                if(temp + pos >= size -1) return times + 1;
            }
            pos =  minIn;
            min = -1;
            times++;
            
        }
        return times;

        
    }
};
