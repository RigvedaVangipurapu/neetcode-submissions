class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        self.output = 0
        maxheight = max(height)
        splitpoint = 0
        for i in range(len(height)):
            if height[i] >= maxheight:
                splitpoint = i
                break
                
        def calcarea(arr, start, end):
            a = 0
            for i in arr[start:end+1]:
                a += (arr[start] - i) if i < arr[start] else 0
            return a
            
        def travtree(arr, left, right, maxright):
            while right <= maxright:
                if arr[right] >= arr[left]:
                    self.output += calcarea(arr, left, right)
                    left = right
                right += 1
                
        travtree(height, 0, 1, splitpoint)
        heightrev = height[::-1]
        travtree(heightrev, 0, 1, len(height) - 1 - splitpoint)
        return self.output
