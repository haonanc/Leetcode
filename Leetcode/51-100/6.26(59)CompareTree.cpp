/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

static int x = [](){ 
    std::ios::sync_with_stdio(false); 
    cin.tie(NULL);  
    return 0; 
}();
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return compare(p,q);
        
    }
    
    bool compare(TreeNode* p, TreeNode* q){
        if(p != nullptr && q != nullptr){
            if(p->val == q->val){
                return (compare(p->left,q->left) && compare(p->right,q->right));
            }
            else return false;
            
        }
        else if(p == nullptr && q == nullptr ) return true;
        else return false;
        
    }
};
