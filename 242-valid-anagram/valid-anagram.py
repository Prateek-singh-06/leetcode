class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        for item in s:
            s1[item]=s1.get(item,0)+1
        for item in t:
            t1[item]=t1.get(item,0)+1
        for key, value in s1.items():
            if(t1.get(key,0)!=value):
                return False
        for key, value in t1.items():
            if(s1.get(key,0)!=value):
                return False
        return True

        