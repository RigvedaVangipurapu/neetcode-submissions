class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left = best = 0
        counts = defaultdict(int)

        for right, char in enumerate(s):
            counts[char] +=1

            while (right - left + 1 - max(counts.values())) > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best,right-left + 1)
        return best
                
