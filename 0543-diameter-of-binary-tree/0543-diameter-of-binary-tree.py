# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # T O(n)  S O(n)
        res = 0 # store the result of largest diameter 

        def depth(root):
            nonlocal res
            # when no node, the depth is zero
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            # we update the diameter with the depth of left + right
            res = max(res, left + right)
            # return the depth of the current node
            return 1 + max(left, right)

        depth(root)
        return res