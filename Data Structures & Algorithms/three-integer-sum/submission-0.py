class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for target_index, target in enumerate(nums):
            # Stop early if target is positive, since remaining numbers are also positive
            if target > 0:
                break

            # 1. Skip duplicate target values
            if target_index > 0 and target == nums[target_index - 1]:
                continue

            # 2. Start left AFTER target_index to avoid re-checking earlier combinations
            left = target_index + 1
            right = len(nums) - 1

            while left < right:
                current_sum = target + nums[left] + nums[right]

                if current_sum == 0:
                    output.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 3. Skip duplicate left and right values after finding a match
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return output
