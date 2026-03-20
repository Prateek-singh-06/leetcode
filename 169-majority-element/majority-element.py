class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majoritylen=len(nums)//2
        majlen=0
        maj=0
        frequency={}
        for i,value in enumerate(nums):
            frequency[value]=frequency.get(value,0)+1
            if(frequency[value]>majoritylen):
                majlen=frequency[value]
                maj=value
        return maj


        # print (majoritylen)
        # return 0
        