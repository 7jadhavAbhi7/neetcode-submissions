class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ls_r=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            j=i+1
            k=len(nums)-1
            print(i,j,k)
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    ls_r.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+nums[i]>0:
                    k-=1
                elif nums[j]+nums[k]+nums[i]<0:
                    j+=1
        
        ls_final=set(map(tuple,[sorted(i) for i in ls_r]))
        ls_final1=list(ls_final)
        ls_final1=list(map(list,ls_final1))
        return ls_final1



        