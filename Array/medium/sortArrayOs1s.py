# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Explanation:
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

class Solution:
    # brutforce
    def sortColorsBruteforce(self, nums: list[int]) -> None:
        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        i = 0

        while count0 > 0:
            nums[i] = 0
            i += 1
            count0 -= 1

        while count1 > 0:
            nums[i] = 1
            i += 1
            count1 -= 1

        while count2 > 0:
            nums[i] = 2
            i += 1
            count2 -= 1

    # optimize three pointer 
    
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        


arr = [0, 1, 2, 2, 1, 1, 0]

s1 = Solution()
s1.sortColors(arr)

print(arr)