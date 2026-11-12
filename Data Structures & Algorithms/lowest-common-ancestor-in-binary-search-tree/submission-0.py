# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findroot( root: TreeNode, p: int, q: int ) -> TreeNode:

            if p == root.val or q==root.val:
                print('i am here', root.val)
                return root

            if p > root.val and q < root.val:
                return root

            if q > root.val and p < root.val:
                return root

            elif p < root.val:
                print('i am here')
                return findroot(root.left, p, q)
            
            else:
                return findroot(root.right, p, q)

            print('i am here', root.val)

        
        return findroot(root, p.val, q.val)



    
        