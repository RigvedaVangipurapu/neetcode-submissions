# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        levels = defaultdict(int)
        level = 0

        if not root:
            return []

        view = []
        q = deque([root])

        while q:
            print(levels)
            level+=1
            for _ in range(len(q)):
                node = q.popleft()
                if level not in levels.keys():
                    view.append(node.val)
                    levels[level] = node.val
                if  node.right:
                    q.append(node.right)
                if  node.left:
                    q.append(node.left)
        print(levels)
        return list(levels.values())



        