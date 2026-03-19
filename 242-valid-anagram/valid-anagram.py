class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set={}
        for item in s:
            s_set[item]=s_set.get(item,0)+1
        for item in t:
            s_set[item]=s_set.get(item,0)-1
        for key, value in s_set.items():
            if(value!=0):
                return False
        return True

        