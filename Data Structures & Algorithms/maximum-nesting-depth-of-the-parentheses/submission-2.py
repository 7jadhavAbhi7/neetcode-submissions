class Solution:
    def maxDepth(self, s: str) -> int:
        ls=[]
        if s.isalpha() or s.isnumeric() or s.isalnum():
            return 0
        m=float('-inf')
        for i in s:
            if i=='(' or i=='{' or i=='[':
                ls.append(i)
            elif i.isnumeric():
                continue
            elif i==')' or i=='}' or i==']':
                m=max(m,len(ls))
                ls.pop()
        return m