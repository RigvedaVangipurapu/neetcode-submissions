# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        trav = []

        if not root:
            return -1

        def traverse(root: Optional[TreeNode]) -> None:
            if not root:
                return

            if root.left:
                trav.append(traverse(root.left))
                
            trav.append(root.val)

            if root.right:
                trav.append(traverse(root.right))

        traverse(root)
        
        trav = [i for i in trav if i is not None]
        return trav[k-1]



        
        