class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        numbers = defaultdict(int)
        numset = set(nums)

        for n in nums:
            counter = 1
            x = n
            if x-1 not in numset:
                while x+1 in numset:
                    counter+=1
                    x+=1
            numbers[n] = counter
        # print(numbers)
        return max(numbers.values())
