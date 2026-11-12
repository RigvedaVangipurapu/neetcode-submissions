class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        for i in nums:
            if i not in counts.keys():
                counts[i] = 1
            else:
                return True
        return False

