class Solution:
    def secondlargestElement(self, nums):
        largest = nums[0]
        secondLargest = -1
        for i in range(len(nums)):
            if(nums[i] > secondLargest): 
                if(nums[i] > largest):
                    secondLargest = largest
                    largest = nums[i]
                elif(nums[i] > secondLargest and nums[i] != largest):
                    secondLargest = nums[i]
                    
 
        return secondLargest

arr = [10 , 10 , 10 ,10 ]
# arr = [8 ,8, 7,6 ,  1]
s1 = Solution()
num = s1.secondlargestElement(arr)
print("second largest number is " , num)