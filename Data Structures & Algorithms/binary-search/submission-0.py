class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        if nums[low] == target:
            return low

        if nums[high] == target:
            return high

        while low <= high:
            mid = int(abs((low + high)/ 2))
            # print(low, mid, high)

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1
        return -1
        