class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lsr=[]
        lsl=[]
        pro=1
        pro1=1
        lsl.append(1)
        for i in range(1,len(nums)):
            pro=pro*nums[i-1]
            lsl.append(pro)
        lsr.append(1)
        for j in range(len(nums)-1,0,-1):
            pro1=pro1*nums[j]
            lsr.append(pro1)
        ls_final=[]
        print(lsl)
        print(lsr)
        for i,j in zip(lsr[::-1],lsl):
            ls_final.append(i*j)
        return ls_final

        
        