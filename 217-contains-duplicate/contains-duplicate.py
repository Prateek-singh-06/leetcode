class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer={}
        for num in nums:
            answer[num]=answer.get(num,0)+1
            if(answer[num]>1):
                return True
        return False
