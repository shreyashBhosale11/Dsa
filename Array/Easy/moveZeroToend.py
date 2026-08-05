# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:
    #shreysh 
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n-1 , - 1 , -1):
            if(nums[i] == 0):
                j = i 
                while(j < n - 1 and nums[j + 1] != 0 ):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
        return nums


    # shreyah 
    def optimizeMoveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        # firstj = 0
        j = -1
        for i in range(n):
            if(j == -1 and nums[i] == 0):
                j = i
                # firstj = 1
            if(nums[i] != 0 and j > -1):
                nums[j] , nums[i] = nums[i] , nums[j]
                j += 1
        return nums
            
    
        

arr = [0 ,1 , 0 , 3 , 12]
s1 = Solution()
# num = s1.moveZeroes(arr)

num = s1.optimizeMoveZeroes(arr)
print("Moved number is " , num)