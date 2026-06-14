class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if s==" " or len(s)==1:
            return 1
        ls=[]
        m=float('-inf')
        for i in range(len(s)):
            if s[i] in ls:
                print(ls)
                while s[i] in ls:
                    ls.pop(0)
                ls.append(s[i])
                m=max(m,len(ls))
                print(ls)
                print(m)
            else:
                ls.append(s[i])
                m=max(m,len(ls))
            
        return m

        