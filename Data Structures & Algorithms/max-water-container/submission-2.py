class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=float('-inf')
        count=0
        while i<=j:
            if heights[i]<heights[j]:
                area=(len(heights)-count-1)*heights[i]
                if m<area:
                    m=area
                i+=1
                print(area)
            
            elif heights[j]<heights[i]:
                area=(len(heights)-count-1)*heights[j]
                if m<area:
                    m=area
                j-=1
                print(area)
            else:
                area=(len(heights)-count-1)*heights[j]
                if m<area:
                    m=area
                j-=1
                print(area)

                
            count+=1
        return m
            