class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = [[]]
        keysdict = defaultdict()

        def convertToTuple(s):
            ans = [0]*26
            for x in s:
                ans[ord(x) - ord('a')] += 1
            return tuple(ans)


        for s in strs:
            smap = convertToTuple(s)
            if smap in keysdict:
                keysdict[smap].append(s)
            else:
                keysdict[smap] = [s]

        return list( keysdict.values()        )

        