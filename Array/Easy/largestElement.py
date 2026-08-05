# Given an array of integers nums, return the value of the largest element in the array
# Example 1
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6

class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for i in range(len(nums)):
            if(nums[i] > largest):
                largest = nums[i]

        return largest


arr = [3 ,3, 6, 1]
s1 = Solution()
num = s1.largestElement(arr)
print("largest number is " , num)