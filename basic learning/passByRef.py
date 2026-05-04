# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
# Example 1
# Input: n=5, arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

class Solution:
    def reverse(self, arr: list) -> None:
        n = len(arr)
        for i in range (n):
            arr[i] , arr[n -i + 1] = arr[n -i + 1] , arr[i]

