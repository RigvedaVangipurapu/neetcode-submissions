class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for s in strs:
            set_s = tuple(sorted([x for x in s]))
            # print(set_s)
            if set_s in groups.keys():
                groups[set_s].append(s)
            else:
                groups[set_s] = [s,]
            # print(groups)
        return list(groups.values())


        
        