class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num1 in enumerate(nums):
            new_target=target-num1
            available=seen.get(new_target,-1)
            if(available!=-1):
                return [i,available]
            seen[num1]=i
        # return [1,2]
        