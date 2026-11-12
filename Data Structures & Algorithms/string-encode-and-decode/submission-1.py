class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        output = ''
        count_output = ''
        counts = {s:len(s) for s in strs}

        for s in strs:
            count_output+= str(counts[s])
            count_output+=','
            output+=s

        return count_output+'#'+output




    def decode(self, s: str) -> List[str]:

        if s=='':
            return []
        # Split only on the first '#' so '#' inside words won't break the split
        header, data = s.split('#', 1)
        
        # Handle the edge case of an empty list of strings
        if not header:
            return []
            
        counts = [int(x) for x in header.split(',') if x!='']
        output = []
        pointer = 0
        
        # Slice each word directly using its exact length
        for count in counts:
            output.append(data[pointer : pointer + count])
            pointer += count
            
        return output



