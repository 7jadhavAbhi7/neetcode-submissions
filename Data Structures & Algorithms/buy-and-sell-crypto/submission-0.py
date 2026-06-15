class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        for i in range(len(prices)-1):
            m=max(m,max(prices[i+1:])-prices[i])        
        if m==0:
            return 0
        return m
            
        