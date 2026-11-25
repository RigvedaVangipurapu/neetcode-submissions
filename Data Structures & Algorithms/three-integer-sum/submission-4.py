class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n - 2):
            # Optional early exit: if the smallest number is > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate starting numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return output
