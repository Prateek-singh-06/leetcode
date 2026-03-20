class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=None
        count=0
        for num in nums:
            if(count==0):
                maj=num
                # coutn+=1
            if(maj==num):
                count+=1
            else:
                count-=1
        return maj
        # majoritylen=len(nums)//2
        # majlen=0
        # maj=0
        # frequency={}
        # for i,value in enumerate(nums):
        #     frequency[value]=frequency.get(value,0)+1
        #     if(frequency[value]>majoritylen):
        #         majlen=frequency[value]
        #         maj=value
        # return maj


        # print (majoritylen)
        # return 0
        