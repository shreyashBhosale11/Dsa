
class Solution:

    def partictionFunction(self , arr , low , high ):
        pivit = arr[low]
        i = low 
        j = high
        while(i < j ):
            while(i <= high and arr[i] <= pivit  ):
                i += 1
            while(j >= low and arr[j] > pivit ):
                j -= 1
            if(i < j ):
                arr[i] , arr[j] = arr[j] , arr[i]
        
        arr[low] , arr[j] = arr[j] , arr[low]
        return j 
            

    def quickSort(self, arr , low , high ):
        if(low < high):
            partiction = self.partictionFunction(arr , low , high )
            self.quickSort(arr , low , partiction -1 )
            self.quickSort(arr , partiction + 1 , high)
        
        
            

        

arr = [7 , 4, 1, 5 , 3]
n = len(arr)
s1 = Solution()
s1.quickSort(arr , 0 , n -1)
print("array is " , arr)