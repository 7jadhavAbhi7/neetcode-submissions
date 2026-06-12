class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        ls=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        hm=dict(sorted(hashmap.items(),key=lambda x:x[1],reverse=True))
        print(hm)
        for k1,v in hm.items():
            if k>0:
                ls.append(k1)
                k-=1
        return ls


        