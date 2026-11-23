class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''
        lens = []
        for i in strs:
            lens.append(str(len(i)))
        # ans = lens + strs
        ans =  '#'.join(lens) + '*' + ''.join(strs)
        return ans


    def decode(self, s: str) -> List[str]:

        if s == '':
            return []
            
        nums_str, words = s.split('*',1)
        nums = [int(i) for i in nums_str.split('#')]

        ans = []
        pointer = 0
        for i in nums:
            ans.append(words[pointer:pointer + i])
            pointer = pointer + i
        # print(ans)
        return ans

