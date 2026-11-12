# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height (root: Optional[TreeNode]) -> int:

            if not root:
                return 0
            
            h = 1

            left_height = height(root.left)
            right_height = height(root.right)
            
            if left_height == -1 or right_height == -1:
                return -1
                
            print(root.val, left_height, right_height)

            if abs(left_height - right_height) > 1:
                return -1

            return h + max( left_height, right_height)
        
        if not root:
            return True

        if height(root) == -1:
            return False
        return True