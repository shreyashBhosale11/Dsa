
class Solution:
    def resurciveinsertionSort(self, nums , i):
        if(i == len(nums) - 1):
                return
        j = i
         
        while(j > 0 and nums[j -1] > nums[j]):
            nums[j- 1] , nums[j] = nums[j] , nums[j- 1]
            j -= 1
        self.resurciveinsertionSort(nums , i+1)
            

        

arr = [7 , 4, 1, 5 , 3]
s1 = Solution()
s1.resurciveinsertionSort(arr , 0)
print("array is " , arr)