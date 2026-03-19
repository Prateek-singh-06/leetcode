class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==1):
            return strs[0]
        minlength=1000
        maxi=len(strs[0])
        for str in strs:
            if(len(str)< minlength):
                minlength=len(str)
        for i in range(minlength):
            base_char=strs[0][i]
            for str in strs:
                if(str[i]!=base_char):
                    return str[0:i]
        return strs[0][0:minlength]

        