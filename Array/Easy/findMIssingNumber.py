# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

# Example 1
# Input: nums = [0, 2, 3, 1, 4]
# Output: 5
# Explanation:
# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2

        for i in range(n):
            expected_sum = expected_sum - nums[i]

        return expected_sum

        
        
            
            