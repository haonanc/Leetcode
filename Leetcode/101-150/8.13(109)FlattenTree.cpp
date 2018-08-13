/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void postOrder(TreeNode* node, TreeNode *&p){
        if(node->right)postOrder(node->right,p);
        if(node->left)postOrder(node->left,p);
        node->right = p;
        node->left = NULL;
        p = node;
    }
    void flatten(TreeNode* root) {
        if(!root) return ;
        TreeNode * p = NULL;
        postOrder(root,p);
           
    }

    
};
