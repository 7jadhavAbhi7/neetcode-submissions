class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[]
        m=float('-inf')
        prefix.append(height[0])
        for i in range(1,len(height)):
            if max(prefix)>height[i]:
                prefix.append(max(prefix))
            else:
                prefix.append(height[i])
        suffix=[]
        suffix.append(height[-1])
        for j in range(len(height)-2,-1,-1):
            if max(suffix)>height[j]:
                suffix.append(max(suffix))
            else:
                suffix.append(height[j])
        suffix.reverse()
        sum=0
        for i in range(len(height)):
            sum+=min(suffix[i],prefix[i])-height[i]
        return sum

        