# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:

    # shreyash bruteforce
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        length = 1
        temp_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i - 1] + 1 == nums[i]:
                temp_length += 1
            else:
                temp_length = 1

            length = max(length, temp_length)

        return length

  
    # chatGpt 
    def longestConsecutiveOptimize(self, nums: list[int]) -> int:
        num_set = set(nums)
        length = 0

        for num in num_set:
            if num - 1 not in num_set:
                temp = num
                temp_length = 1

                while temp + 1 in num_set:
                    temp += 1
                    temp_length += 1
 
                length = max(length, temp_length)

        return length


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

s1 = Solution()
print(s1.longestConsecutiveOptimize(nums))  # 9






nums = [0,3,7,2,5,8,4,6,0,1]
s1 = Solution()
num = s1.longestConsecutive(nums)
print(num)


