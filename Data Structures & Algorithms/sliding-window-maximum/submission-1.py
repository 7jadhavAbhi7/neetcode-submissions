class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        m=float('-inf')
        ls=[]
        for i in range(k):
            d.append(nums[i])
        if max(d)>m:
            ls.append(max(d))
        print(d)
        for i in range(k,len(nums)):
            d.popleft()
            d.append(nums[i])
            if max(d)>m:
                ls.append(max(d))
        return ls
                