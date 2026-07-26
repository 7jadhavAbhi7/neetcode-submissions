class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ls=[0]*len(nums)
        for i in nums:
            ls[i]+=1
        print(ls)
        for i,j in enumerate(ls):
            if j>1:
                return i        