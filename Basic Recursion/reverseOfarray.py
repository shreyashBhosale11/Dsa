# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# Example 1
# Input: n=5, arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]




class Solution:
    def reverse(self, arr, left, right):
        if left >= right:
            return

        arr[left], arr[right] = arr[right], arr[left]

        self.reverse(arr, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]

s1 = Solution()
s1.reverse(arr, 0, len(arr) - 1)

print(arr)
