# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

# Example 1
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1
# Explanation:
# The first occurence of 3 in nums is at index 1

class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if(nums[i] == target):
                return i

        return -1
arr = [3 ,3, 6, 1]
s1 = Solution()
num = s1.linearSearch(arr , 6)
print("number is  at index " , num)