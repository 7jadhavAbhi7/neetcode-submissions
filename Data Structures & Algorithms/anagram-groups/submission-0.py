class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap={}

        for i in strs:
            ls1=sorted(i)
            str1="".join(ls1)
            if str1 not in hashmap:
                hashmap[str1]=[i]
            else:
                ls=hashmap.get(str1)
                print(ls)
                ls.append(i)
                hashmap[str1]=ls
        ls_result=[]
        for k,v in hashmap.items():
            ls_result.append(v)
        return ls_result



        