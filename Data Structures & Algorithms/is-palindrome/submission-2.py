class Solution:
    def isPalindrome(self, s: str) -> bool:


        s_list = [i.lower() for i in s if i!=' ' and i.isalnum()]
        start = 0
        end = len(s_list)
        mid = int((start + end)/2)

        if len(s_list)==0:
            return True

        print(start, end, mid)

        for i in range(start, mid+1):
            if s_list[start] != s_list[end-1]:
                print(start, end, s_list[start], s_list[end-1])
                return False
            start+=1
            end-=1
        return True

        
        