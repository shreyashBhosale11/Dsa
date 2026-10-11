# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

class Solution:
    # brute force Shreyash 
    def maxSubArray(self, nums: list[int]) -> int:
        maxum = nums[0]
    
        for i in range(len(nums) - 1 ):
            sum = nums[i]
            for j in range(i +1  , len(nums)):
                sum += nums[j]
                if(sum >= maxum):
                    maxum = sum
        return maxum


    # optimize chatgpt
    def maxSubArrayOptimize(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1 , len(nums)):
            current_sum = max(nums[i] , nums[i] + current_sum)
            max_sum = max(max_sum , current_sum)
        return max_sum



            

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
s1= Solution()
print(s1.maxSubArray(nums))
print(s1.maxSubArrayOptimize(nums))

                

