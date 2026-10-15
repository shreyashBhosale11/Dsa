# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

# Example 1:
# Input : nums = [4, 2, 2, 6, 4], k = 6

# Output : 4

# Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]


class Solution:
    # Shreyash BruteForce
    def subarraysWithXorK(self, nums, k):
        count = 0
        n = len(nums)

        for i in range(n):
            result = 0
            for j in range(i , n):
                result = result ^ nums[j]
                if(result == k):
                    count += 1

        return count 


    # shreyash and Striver Optimal
    def subarraysWithXorKOpitimize(self, nums, k):
        count = 0
        n = len(nums)
        prefix_xor = 0
        hash = {0:1}

        for i in range(n):
            prefix_xor ^= nums[i]
            rem = prefix_xor ^ k

            if rem in hash:
                count += hash[rem]

            hash[prefix_xor] =hash.get(prefix_xor ,0 ) + 1


        return count 


nums = [4, 2, 2, 6, 4]
k = 6
s1 = Solution()
count = s1.subarraysWithXorK(nums , k)
count1 = s1.subarraysWithXorKOpitimize(nums , k)
print(count1)