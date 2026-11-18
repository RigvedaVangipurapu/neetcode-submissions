class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = defaultdict()

        for i,n in enumerate(nums):
            # print(i,n)
            if target - n in visited:
                return[visited[target-n], i]
            visited[n] = i
        return [-1,-1]
        