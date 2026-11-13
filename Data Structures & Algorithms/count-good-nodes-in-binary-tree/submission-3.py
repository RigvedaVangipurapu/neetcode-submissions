# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        if not root:
            return 0

        stack = [(root, root.val)]
        maxval = root.val

        while stack:
            node, maxval = stack.pop()
            if node.val >= maxval:
                good_nodes+=1
                maxval  = node.val
            
            if node.left:
                    stack.append((node.left, max(node.left.val , maxval)))
            if node.right:
                    stack.append((node.right, max(node.right.val , maxval)))
        return good_nodes

            




        