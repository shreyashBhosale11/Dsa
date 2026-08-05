class Solution:
#     Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


# Example 1

# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation:

# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.
    # some shreyash some gpt
    
    def longestSubarray(self, nums, k):
        prefixMap = {}
        prefixSum = 0
        maxLen = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum == k:
                maxLen = i + 1

            if (prefixSum - k) in prefixMap:
                length = i - prefixMap[prefixSum - k]
                maxLen = max(maxLen, length)

            if prefixSum not in prefixMap:
                prefixMap[prefixSum] = i

        return maxLen


arr = [10, 5, 2, 7, 1, 9]

s1 = Solution()
print(s1.longestSubarray(arr, 15))