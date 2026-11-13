# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.preorder_index = 0

        self.in_map = { v: i for i,v in enumerate(inorder)}

        #preorder = [1,2,3,4], 
        #inorder = [2,1,3,4]-- pre order tells us the root, in order tells us left vs right
        #in_map = {2: 0, 1:1, 3:2, 4:3}

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return 

            nodeval = preorder[self.preorder_index]
            node = TreeNode(nodeval)

            mid = self.in_map[nodeval]

            self.preorder_index += 1

            # print(left,mid,right, nodeval)
            
            node.left = build(left, mid - 1)
            node.right = build(mid+1, right)
            return node
            


        return build(0,len(preorder)-1)


            
        