class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        right = 0
        s1_freq = Counter(s1)
        print(s1_freq)

        for left, letter in enumerate(s2):
            # print(letter)
            match_freq = defaultdict(int)
            if letter in s1_freq.keys():
                right = left

                while right - left + 1 <= len(s1) and right < len(s2):

                    right_letter = s2[right]
                    print(letter, right_letter)
                    if right_letter not in s1:
                        break

                    elif match_freq[right_letter] == s1_freq[right_letter]:
                        break
                    
                    else:
                        match_freq[right_letter] += 1
                        if right - left + 1 ==len(s1):
                            return True
                        right+=1
        return False

