class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftprod = [1] * n
        rightprod = [1] * n

        # Populate left products (left to right)
        for i in range(1, n):
            leftprod[i] = leftprod[i - 1] * nums[i - 1]

        # Populate right products (right to left)
        for i in range(n - 2, -1, -1):
            rightprod[i] = rightprod[i + 1] * nums[i + 1]

        output = []
        for i in range(n):
            output.append(leftprod[i] * rightprod[i])

        return output
