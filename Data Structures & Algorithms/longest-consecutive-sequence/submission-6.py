class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq = 0

        starters = set()
        for i in set_nums:
            if i-1 not in set_nums:
                starters.add(i)

        for i in starters:
            counter = 1
            num = i
            while num + 1 in set_nums:
                counter += 1
                num += 1
            max_seq = max(max_seq, counter)
        return max_seq 
        