# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    # shreyash 
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        prevHigh = -1 
        count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count += 1 
            else:
                if(prevHigh < count):
                    prevHigh = count
                    count = 0
                else:
                    count = 0
        return max(prevHigh , count)

    def findMaxConsecutiveOnesSecondApproch(self, nums):
        count = 0
        maximum = 0

        for num in nums:
            if num == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0

        return maximum


arr = [1 , 0 , 1, 1, 1]
s1 = Solution()
value = s1.findMaxConsecutiveOnes(arr)
print("this is the maximum Consicative value one " , value)


