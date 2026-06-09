class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls=list(s)
        ls1=list(t)
        print(ls)
        print(ls1)
        if sorted(ls)==sorted(ls1):
            return True
        return False

        