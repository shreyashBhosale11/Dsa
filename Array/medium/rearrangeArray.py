# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions. 
class Solution:

    # better approch Shreyash 
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arrPostive = []
        arrnegative = []

        for num in nums:
            if(num < 0):
                arrnegative.append(num)
            else:
                arrPostive.append(num)

        itrp = 0
        itrn = 0

        for i in range(n):
            if(i % 2 == 0):
                nums[i] = arrPostive[itrp]
                itrp += 1
            else:
                nums[i] = arrnegative[itrn]
                itrn += 1
        return nums

    # optimize Shreyash + gpt 
    def rearrangeArrayOptimize(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2

        return result

s1 = Solution()
arr =[3,1,-2,-5,2,-4]

nums = s1.rearrangeArrayOptimize(arr)
print(nums)
