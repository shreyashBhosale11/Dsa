
class Solution:
    def mergeSort(self, nums , low ,high):

        if(low >= high): return
        mid = (low + high)// 2

        self.mergeSort(nums , low , mid)
        self.mergeSort(nums ,mid + 1 , high)
        self.merge(nums , low , mid , high )


    def merge(self ,nums , low , mid , high ):
        tem = []
        left = low 
        right = mid + 1 

        while(left <= mid and right <= high):
            if(nums[left] <= nums[right]):
                tem.append(nums[left])
                left += 1
            else:
                tem.append(nums[right])
                right += 1

        while(left <= mid):
            tem.append(nums[left])
            left += 1

        while(right <= high):
                tem.append(nums[right])
                right += 1

        for i in range(low , high + 1):
            nums[i] = tem[i - low]

        return nums
    

arr = [7 , 4, 1, 5 , 3 , 6 , 8, 9]
s1 = Solution()
s1.mergeSort(arr, 0, len(arr) - 1)
print(arr)

        

