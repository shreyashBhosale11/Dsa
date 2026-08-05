# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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


arr = [2 ,7, 11, 15]
s1 = Solution()
num = s1.twoSum(arr , 9)
print("targeted index are  " , num)
                
