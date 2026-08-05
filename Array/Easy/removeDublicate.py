class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        large = nums[0]
        j = 1
     
        for i in range( 0, len(nums)):
            if(large < nums[i]):
                large = nums[i]
                nums[j] , nums[i] = nums[i] , nums[j]
                
                j+= 1
        return j

arr = [1 , 1, 2, 2 ,3 ,3 ,  4 , 5 , 5]
s1 = Solution()
k = s1.removeDuplicates(arr)
print("value of k is " , k)