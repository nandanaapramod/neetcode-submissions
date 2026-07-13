class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        out=0
        i=0
        j=len(heights)-1

        while i<j:
            area=min(heights[i],heights[j])*(j-i)
            out=max(out,area)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return out
