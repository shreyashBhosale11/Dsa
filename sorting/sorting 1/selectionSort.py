# Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
# Example 1
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            for j in range( i,len(nums)):
                if(nums[i] > nums[j]):
                    nums[i] , nums[j] = nums[j] , nums[i]

        print("array is " , nums)

arr = [7 , 4, 1, 5 , 3]
s1 = Solution()
s1.selectionSort(arr)

