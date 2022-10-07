# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case, return when null
        if not root:
            return 
        # swap left and right nodes
        temp = root.left
        root.left = root.right
        root.right = temp
        # call function on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root