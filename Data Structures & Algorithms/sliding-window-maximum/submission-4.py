class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        currmap = defaultdict(int)
        maxnums = []
        tempmax = nums[0]

        left = 0
        right = k-1

        def calcmax(d):
            # print('calculating max', d)
            maxval = float('-inf')
            for k,v in d.items():
                maxval = max(k,maxval) if v > 0 else maxval

            return maxval


        while right < len(nums):
            if left == 0:
                for i in range(left, right+1):
                    currmap[nums[i]] += 1
                    tempmax = max(tempmax , nums[i])
                maxnums.append(tempmax)
                
            else:
                currmap[nums[right]] += 1
                deleted = nums[left-1]
                currmap[deleted] -= 1
                tempmax = calcmax(currmap)
                maxnums.append(tempmax)
            # print(left,right, maxnums, currmap)

                
            left += 1
            right = left + k -1
        return maxnums


        