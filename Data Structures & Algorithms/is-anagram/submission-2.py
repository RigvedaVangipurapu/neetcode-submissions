class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict.fromkeys(list(s),0)
        for i in s:
            d[i]+=1
        print(d)
        
        for i in t:
            if i not in d.keys():
                return False
            d[i]-=1
        
        if any(value != 0 for value in d.values()):
            return False
        return True
            
