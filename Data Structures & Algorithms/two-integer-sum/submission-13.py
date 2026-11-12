class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)<3:
            return [0,1]

        num_dict = dict()

        for i in range(len(nums)):
            # i = nums.index(num)
            num = nums[i]
            j = nums.index(target - num) if (target-num) in nums else -1
            print(i,j)
            if j>=0 and i!=j:
                print(i,j)
                return list(sorted([i,j]))
            num_dict[num] = i


