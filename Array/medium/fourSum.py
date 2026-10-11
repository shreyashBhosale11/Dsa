# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

class Solution:

    # better approch by distonry 
    def fourSumBetter(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        
        n = len(nums)
        for i in range(n):

            for j in range(i+1 , n):
                setup = {}

                for k in range(j+1 ,n):
                    sum = nums[i] + nums[j] + nums[k]
                    fourth = target - sum 

                    if fourth in setup:
                        temp = [nums[i] , nums[j] , nums[k] , fourth]
                        temp.sort()

                        if temp not in result:
                            result.append(temp)

                    setup[nums[k]] = k


        return result


    # Optimize Striver     Time: \(O(n^3)\) # Auxiliary space: \(O(1)\)
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-3):
            if(i > 0 and nums[i] == nums[i-1]) :continue

            for j in range(i+1 , n-2):
                if(j > i + 1 and nums[j] == nums[j-1]) :continue

                left = j + 1
                right = n - 1
                while(left < right):
                    sumNum = nums[i] + nums[j]+ nums[left] + nums[right]
                    if(sumNum == target):
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        result.append(temp)
                        left += 1
                        right -=1 

                        while(left < right and nums[left] == nums[left- 1]):
                            left += 1
                        while(left < right and nums[right] == nums[right + 1]):
                            right -= 1

                    elif(sumNum < target):
                        left += 1
                    else:
                        right -=1 

        return result


                 
nums = [1, 0, -1, 0, -2, 2]
target = 0   

s1 = Solution()
num = s1.fourSum(nums , target)
print(num)