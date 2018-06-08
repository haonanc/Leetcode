class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> re;
        if(nums.size()<3){
            return re;
        }
        sort(nums.begin(),nums.end());
        int a = 0;
        int b = 1;
        int c = 2;
        set<int> sa;
        set<int> sb;
        set<int> sc;
        while(a < nums.size() -2){
            if(sa.count(nums[a])){
                a ++;
                b = a+1;
                c = b + 1;
            }
            else{
                            sa.insert(nums[a]);
            sb.clear();
            while(b < nums.size() -1){
                if(sb.count(nums[b])){
                    b++;
                    c = b+1;
                }
                else{
                    sb.insert(nums[b]);
                sc.clear();
                while(c < nums.size()){
                    if(sc.count(nums[c])){
                        c++;         
                    }
                    else{
                        sc.insert(nums[c]);
                    if(nums[a]+nums[b]+nums[c] == 0){
                        vector<int> *v = new vector<int>;
                        v->push_back(nums[a]);
                        v->push_back(nums[b]);
                        v->push_back(nums[c]);                 
                        re.push_back(*v);
                    }
                    c++;          
                    }  
                }
                b++;
                c = b+1;                    
                }
                
            }

            a ++;
            b = a+1;
            c = b + 1;
                
            }

        }
        return re;
        
    }
};
