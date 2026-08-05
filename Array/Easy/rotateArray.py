# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    # shreyash approch 
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        rotation = k % n  
        
        
        while(rotation > 0):
            temp = nums[n-1]
            for i in range(n):
                temInLoop = nums[i]
                nums[i] = temp
                temp = temInLoop 
            rotation -= 1
        return nums


    def reverse(self , arr , big , end ):
        left = big 
        right = end 
        while(left < right):
            arr[left] , arr[right] = arr[right] , arr[left]
            left += 1
            right -= 1

        return arr



    def rotateBYReverse(self, nums: list[int], k: int) -> None:
        n = len(nums)
        d = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, d - 1)
        self.reverse(nums, d, n - 1)
        return nums


arr1 = [1 , 2, 3, 4, 5,6 ,7 ]
arr2 = [1 , 2, 3, 4, 5,6 ,7 ]


s1 = Solution()
num1 = s1.rotate(arr1 , 3)
num2 = s1.rotateBYReverse(arr2 , 3)

print("largest number is " , num1  )
print("largest number is " , num2  )

    

        
        