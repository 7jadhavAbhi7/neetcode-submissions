class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=list(s)
        ls1=[i for i in s if i.isalnum()]
        s1="".join(ls1)
        
        i=0
        j=len(s1)-1
        print(s1)
        while i<=j:
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True
        