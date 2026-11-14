class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        t_map = dict(Counter(t))
        s_map = defaultdict(int)

        if len(s) < len(t):
            return ''

        left, right = 0 , 0

        def isValid(d1,d2):
            for i, count in d2.items():
                if i not in d1.keys() or  count > d1[i]:
                    return False
            return True
            

        answer = s

        for right, letter in enumerate(s):
            if letter in t_map.keys():
                s_map[letter]+=1
            
            if isValid(s_map , t_map):
                while left <= right:

                    left_letter = s[left]

                    if left_letter not in t_map.keys():
                        left += 1
                    
                    elif s_map[left_letter] > t_map[left_letter]:
                        s_map[left_letter] -= 1
                        left += 1

                    else:
                        answer = s[left:right+1] if len(answer) > len(s[left:right+1]) else answer
                        break

        return answer if isValid(s_map, t_map) else ''

                    

                

        



