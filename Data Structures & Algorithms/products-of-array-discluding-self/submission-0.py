class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prev_prod = defaultdict(int)
        next_prod = defaultdict(int)
        ans = defaultdict(int)
        prev_prod[0] = 1
        next_prod[len(nums)-1] = 1

        for i in range(1,len(nums)):
            prev_prod[i] = prev_prod[i-1]* nums[i-1]
        # print(prev_prod)

        for i in range(len(nums)-2,-1,-1):
            next_prod[i] = next_prod[i+1]*nums[i+1]
        # print(next_prod)

        for i in prev_prod.keys():
            ans[i] = prev_prod[i]*next_prod[i]
        
        return list(ans.values())
