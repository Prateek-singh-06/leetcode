class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for elem in nums:
            if(elem!=val):
                nums[k]=elem
                k+=1

        return k

            
            
