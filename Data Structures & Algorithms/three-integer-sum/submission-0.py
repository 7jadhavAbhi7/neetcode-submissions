class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sum1=0
        
        ls_final=[]
        nums.sort()
        for k in range(len(nums)-1):
            i=k+1
            j=len(nums)-1
            ls=[]
            while i<j:
                if nums[i]+nums[j]+nums[k]==0:
                    ls_final.append([nums[i],nums[j],nums[k]])
                    i+=1;
                    j-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    i+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    j-=1
        ls_final=[sorted(i) for i in ls_final]
        s=set()
        for i in ls_final:
            s.add(tuple(i))
        final=list(map(list,s))
        
        return final

