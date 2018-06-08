class Solution {
public:
int longestValidParentheses(string s) {
        int l = 0, r = 0, res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') l++;
            else r++;
            if (l == r) res = max(res, 2 * r);
            else if (r > l) l = r = 0;
        }
        l = r = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == '(') l++;
            else r++;
            if (l == r) res = max(res, 2 * l);
            else if (l > r) l = r = 0;
        }
        return res;
    }
};
