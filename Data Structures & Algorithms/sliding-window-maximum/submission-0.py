class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ls=[]
        for k1 in range(0,len(nums)-k+1):
            ls.append(max(nums[k1:k1+k]))
        return ls

            
        