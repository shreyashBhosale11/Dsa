# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 # Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

arr = [1 , 2 , 4 ,2  , 1]
# arr = [8 ,8, 7,6 ,  1]
s1 = Solution()
num = s1.singleNumber(arr)
print("second largest number is " , num)

        