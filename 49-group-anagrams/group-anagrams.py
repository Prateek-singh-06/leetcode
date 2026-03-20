class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        visited={}
        sortedstrarr=[]
        for i,str1 in enumerate(strs):
            str2=''.join(sorted(str1))
            sortedstrarr.append(str2)
            if(visited.get(str2,0)==0):
                visited[str2]=[]
            visited[str2].append(str1)
            # print(visited[str2])
        for key,value in visited.items():
            ans.append(value)
        return ans
        # retrun [["abc","afbj"],["jahf","jhfbj"]]        