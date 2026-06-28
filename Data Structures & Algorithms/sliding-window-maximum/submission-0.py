class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sum=0
        ls=[]
        m=float('-inf')
        final_result=[]
        for i in range(k):
            ls.append(nums[i])
        if m<max(ls):
            final_result.append(max(ls))
        i=0
        for j in range(k,len(nums)):
            ls.pop(0)
            ls.append(nums[j])
            if m<max(ls):
                final_result.append(max(ls))

        return final_result
        