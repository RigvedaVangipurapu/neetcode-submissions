class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 1

        left = 0
        right = 1

        maxsub = 1
        seen = set(s[left])

        counter = 0

        while right < len(s) and left <=right:
            # print(seen, 'left', left, 'right', right)
            if s[right] in seen:
                maxsub = max(right - left, maxsub)
                seen.remove(s[left])
                left += 1

            else:
                seen.add(s[right])
                right += 1
        return max(maxsub, right-left )
            



         

        



        