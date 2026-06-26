class Solution:
    def countBits(self, n: int) -> List[int]:
        ls=[]
        for i in range(n+1):
            count=0
            while i>0:
                i=i&(i-1)
                count+=1
            ls.append(count)
        print(ls)
        return ls
        