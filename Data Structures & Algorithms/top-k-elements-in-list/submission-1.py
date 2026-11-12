class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counts = dict(Counter(nums))

        return list(sorted(counts, key = lambda n : counts[n], reverse = True))[:k]        
