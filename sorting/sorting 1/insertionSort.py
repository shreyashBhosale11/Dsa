# Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
# Example 1
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

class Solution:
    def insertionSort(self, nums):
        for i in range(len(nums)):
            j = i
            while(j > 0 and nums[j -1] > nums[j]):
                nums[j- 1] , nums[j] = nums[j] , nums[j- 1]
                j -= 1

        print("array is " , nums)

arr = [7 , 4, 1, 5 , 3]
s1 = Solution()
s1.insertionSort(arr)