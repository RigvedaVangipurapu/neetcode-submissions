class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return float('-inf')

        self.globalmax = float('-inf')

        def findmax(node: TreeNode) -> tuple:

            if not node:
                return (0, 0)

            if not node.left and not node.right:
                self.globalmax = max(self.globalmax, node.val)
                return (node.val, 1)

            leftval, leftflag = findmax(node.left) if node.left else (0, 0)
            rightval, rightflag = findmax(node.right) if node.right else (0, 0)

            leftgain = max(0, leftval * leftflag)
            rightgain = max(0, rightval * rightflag)

            if node.val >= 0:
                winner = max(
                    node.val,
                    node.val + leftgain,
                    node.val + rightgain
                )

                self.globalmax = max(
                    self.globalmax,
                    winner,
                    node.val + leftgain + rightgain
                )

                return (winner, 1)

            if node.val < 0:
                flagneg = 1

                winner1 = max(
                    node.val,
                    node.val + leftgain,
                    node.val + rightgain
                )

                winner2 = max(leftval, rightval)

                # Cannot return winner2 because it skips node
                winner = winner1

                self.globalmax = max(
                    self.globalmax,
                    winner,
                    node.val + leftgain + rightgain
                )

                return (winner, flagneg)

        findmax(root)
        return self.globalmax