class Solution:
    def bubbleSort(self, nums , n ):
        
        if( n == 1):
            return
        did_swap = False
        for j in range(n-1):
            if(nums[j] >= nums[j+1]):
                nums[j], nums[j+1] = nums[j+1 ] , nums[j]
                did_swap = True
                
        self.bubbleSort(nums , n-1)

        if not did_swap:
            return




        
            