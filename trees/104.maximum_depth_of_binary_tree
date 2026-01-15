# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        # 2. Recursive Step: Ask for the max depth of the left and right children
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 3. Logic: The depth of the current node is 1 (itself) 
        # plus whichever child path is deeper.
        return max(left_depth, right_depth) + 1