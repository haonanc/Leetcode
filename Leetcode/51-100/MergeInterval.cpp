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
        bool flag = true;
        set<string> se;
        Interval c;
        for(Interval i:intervals){
            flag = true;
            int s = i.start;
            int e = i.end;
            int count = 0;
            while(count < ret.size()){
                
                Interval&c =ret[count];
                if(s <= c.end && c.start<=e){
                    se.erase(to_string(c.start)+";"+to_string(c.end));
                    c.start = min(c.start,s);
                    c.end = max(c.end,e);
                    flag = false;
                    string str = to_string(c.start)+";"+to_string(c.end);
                    if(se.count(str) ==1){
                        cout <<count<<"D";
                        count --;
                        ret.erase(ret.begin()+count);
                    }
                    else {
                        cout <<count<<"C";
                        se.insert(str);
                    }
                }
                count ++;
                
            }
                
            
            if(flag){
                cout <<"push";
                Interval temp(s,e); 
                se.insert(to_string(s)+";"+to_string(s));
                ret.push_back(temp);
            }
        }
        return ret;
        
        
    }
};
