# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:

            node, minval, maxval = stack.pop()
            # print(node.val, maxval, minval)

            if node.val >= maxval or node.val <= minval:
                return False
            
            if  node.left:
                stack.append((node.left, minval, node.val))
            
            if  node.right:
                stack.append((node.right, node.val, maxval))

        return True

        





            
        