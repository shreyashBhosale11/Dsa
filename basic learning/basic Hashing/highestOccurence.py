# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.


class Solution:
    # shreyash 
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        maxi = 1
        for i in range(len(nums)-1 , -1, -1):
            comp = nums[i]
            counter = 1
            k_value = k
            for j in range(i-1 , -1 , -1):
                value = comp - nums[j]
                if(value <= k_value and value >= 0):
                    k_value = k_value - value
                    counter += 1
                    maxi = max(maxi , counter)
                else:
                    break

            return maxi

    # chatgpt
    def optimizeMaxFrequency(self, nums: list[int], k: int) -> int:

        nums.sort()

        left = 0
        total = 0
        ans = 0

        for right in range(len(nums)):

            total += nums[right]

            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# arr = [1, 2, 4]
arr = [1, 4, 8 , 13 ]

s1 = Solution()
nums1 = s1.maxFrequency(arr , 5)
print("maximum frequency ",nums1)

                


                