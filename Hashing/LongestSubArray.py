# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Example 1:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation:

# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Example 2:



class Solution:
    # hashing approch 
    def subarraySumHash(self, nums: list[int], k: int) -> int:
            hash = {}
            sum = 0 
            max_len = 0
            for i in range(len(nums)):
                sum += nums[i]
                if(sum == k):
                    max_len = max(max_len , i+ 1)
                rem = sum - k
                if rem in hash:
                    len = i - hash[rem] 
                    max_len = max(max_len , len)
                hash[sum] = i
                                    
                     

                 



    def subarraySum(self, nums: list[int], k: int) -> int:
        left = 0
        current_sum = 0
        length = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > k and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == k:
                length = max(length, right - left + 1)

        return length

        