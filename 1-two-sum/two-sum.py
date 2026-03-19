class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num1 in enumerate(nums):
            new_target=target-num1
            for j,num2 in enumerate(nums):
                if(j!=i and num2==new_target):
                    ans=[i,j]
                    # ans.append(i)
                    # ans.append(j)
                    return ans
            # print(i)
        # return [1,2]
        