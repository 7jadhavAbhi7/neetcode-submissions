class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=float('-inf')
        while i<=j:
            if heights[i]==heights[j]:
                capacity=heights[i]*(j-i)
                m=max(m,capacity)
                i+=1
                j-=1
            elif heights[i]<heights[j]:
                capacity=heights[i]*(j-i)
                m=max(m,capacity)
                i+=1
            elif heights[j]<heights[i]:
                capacity=heights[j]*(j-i)
                m=max(m,capacity)
                j-=1
        return m




        