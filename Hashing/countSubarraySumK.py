# iven an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

class Solution:

    # optimize gpt 
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_freq = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            rem = prefix_sum - k

            if rem in prefix_freq:
                count += prefix_freq[rem]

            prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1

        return count
        