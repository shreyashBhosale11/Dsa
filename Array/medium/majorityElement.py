# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    # better approch shreyash 
    def majorityElementBetter(self, nums: list[int]) -> int:
        counter = {}
        half = len(nums)// 2
        for i in range(len(nums)):
            if nums[i] in  counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        for num in counter:
            if(counter[num] > half):
                return num
        return 0    

    #optimize approch
    def majorityElementOptmize(self, nums: list[int]) -> int:
        candidate = 0 
        count = 0

        for num in nums:
            if(count == 0):
                candidate = num
            if(candidate == num):
                count += 1
            else:
                count -= 1
        return candidate


arr = [2, 2, 1, 1, 1, 2, 2]
s1 = Solution()
# print(s1.majorityElement(arr))
print(s1.majorityElementOptmize(arr))


