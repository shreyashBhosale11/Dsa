# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1

class Solution:
    # brought force approch 
    def twoSumBroutforce(self, nums: list[int], target: int) -> list[int]:
        
         
        for i in range(len(nums)- 1):
            sum = 0
            for j in range(i+ 1 , len(nums)):
                sum = nums[i] + nums[j]
                if(sum == target ):
                    return i , j
            







    def twoSumSorted(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        i = 0
        j = n-1 
        while(i < j ):
            sum = nums[i] + nums[j]
            if(sum == target):
                return i , j
            if(sum > target):
                if(nums[i] < nums[j]):
                    j -= 1
                else:
                    i += 1
            if(sum < target):
                if(nums[i] < nums[j]):
                    i += 1
                else:
                    j -= 1

    # optimize approch by distionry 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i



arr = [2 ,7, 11, 15]
s1 = Solution()
# num = s1.twoSum(arr , 9)
br1 = s1.twoSumBroutforce(arr , 26)
opty= s1.twoSum(arr , 9)
# print("targeted index are  " , num)
print("targeted index are  " , opty)

                
