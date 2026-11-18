from collections import Counter, defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_counts = Counter(nums)
        
        # Group numbers by their frequency
        count_nums = defaultdict(list)
        for num, freq in num_counts.items():
            count_nums[freq].append(num)
            
        # Create buckets where index = frequency (1 to n)
        buckets = [[] for _ in range(n + 1)]
        for freq, num_list in count_nums.items():
            buckets[freq] = num_list
            
        # Collect elements from highest frequency down to 1
        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
