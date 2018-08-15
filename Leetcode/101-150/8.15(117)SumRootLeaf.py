class Solution(object):
    def sumNumbers(self, root):
        return recursion(root,"")
        """
        :type root: TreeNode
        :rtype: int
        """
def recursion(node,cur):
    if node == None:
        return 0
    new = cur+str(node.val)
    if node.left == None and node.right == None:
        return int(cur+str(node.val))
    return recursion(node.left,new)+recursion(node.right,new)
