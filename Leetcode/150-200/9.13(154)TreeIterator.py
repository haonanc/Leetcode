# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        """
        :type root: TreeNode
        """
        

    def hasNext(self):
        return self.stack != []
        """
        :rtype: bool
        """
        

    def next(self):
        temp = self.stack[-1]
        root = temp.right
        self.stack.pop()
        while root:
            self.stack.append(root)
            root = root.left
        return temp.val
        
        
        """
        :rtype: int
        """
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
