/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> ret;
        int count = 0;
        int merge = 0;
        int index = 0;
        while(count < intervals.size()){     
            
            index = count;
            merge = count - 1;
            while(merge >= 0){
            Interval &i = intervals[index];
            int s = i.start;
            int e = i.end;
            Interval &c = intervals[merge];

            if(s <= c.end && c.start<=e){
            c.start = min(c.start,s);
            c.end = max(c.end,e);
            intervals.erase(intervals.begin()+index);
            count --;
            index = merge;
            merge --;
                
            }
            else merge--;
                
            }
            
            count ++;
                
                
                
                
            
            
            
        }
        return intervals;
        
    }
};
