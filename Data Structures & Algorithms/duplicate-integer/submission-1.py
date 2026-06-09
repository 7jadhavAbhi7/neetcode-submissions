class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for k,v in hashmap.items():
            if v>1:
                return True
        return False
        