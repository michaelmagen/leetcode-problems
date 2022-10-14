# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs T O(n) S O(n)
        # if both nodes null then they the same 
        if not p and not q:
            return True
        # trees dont have same structure of same value
        if not p or not q or p.val != q.val:
            return False
        # need both subtrees to return true
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 