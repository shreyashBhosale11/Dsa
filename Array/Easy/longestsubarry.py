# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Example 1
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4
# Explanation:
# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

class Solution:
    # some shreyash some gpt
    def longestSubarray(self, nums, k):
        
        i = 0
        currentSum = 0
        maxLength = 0

        for j in range(len(nums)):
            currentSum += nums[j]

            while currentSum > k:
                currentSum -= nums[i]
                i += 1

            if currentSum == k:
                maxLength = max(maxLength, j - i + 1)

        return maxLength
            



