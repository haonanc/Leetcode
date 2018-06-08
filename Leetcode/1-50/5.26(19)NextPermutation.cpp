class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if(len <2) return;
        int temp;
        int last = nums[len-1];
        int index = len-2;
        int secondlast= nums[index]; 
        int lowestValue;
        int lowestIndex;
        int indexToSwap;
        int valueToSwap;
        //case 1, regular swap
        if(secondlast < last){
            temp = secondlast;
            nums[len-2] = nums[len-1];
            nums[len-1] = temp;
            return;
        }
        index --;
        while(index >= 0){

            if(nums[index]>=nums[index + 1]) index --;
            else{
                lowestIndex = index + 1;
                lowestValue = nums[index + 1];
                indexToSwap = index;
                valueToSwap = nums[index];
                index = index + 2;
                while(index < len){
                    if(nums[index]>valueToSwap && nums[index]<lowestValue){
                        lowestValue = nums[index];
                        lowestIndex = index;
                    }
                    index++;
                }
                //swap
                nums[lowestIndex] = valueToSwap;
                nums[indexToSwap] = lowestValue;
                
                sort(nums.begin()+indexToSwap + 1, nums.end());
                return;
            }
            
            
        }
        sort(nums.begin(),nums.end());
        
        
        //case 2, shift with previous item, 
        
        
    }
};
