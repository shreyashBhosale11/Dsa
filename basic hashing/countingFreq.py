# Given an array nums of size n which may contain duplicate elements.
# Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.
# You may return the result in any order, but each element must appear exactly once in the output.

# Example 1
# Input: nums = [1, 2, 2, 1, 3]
# Output: [[1, 2], [2, 2], [3, 1]]
# Explanation:
# - 1 appears 2 times
# - 2 appears 2 times
# - 3 appears 1 time
# Order of output can vary.





# class Solution:
#     def countFrequencies(self, nums):
#         maxi = max(nums)
#         hash = [0] * (maxi + 1)

#         for i in range(len(hash)):
#             hash[nums[i]] +=1
        
#         ans = []
#         for i in range(len(hash)):
#             if hash[i] != 0:
#                 ans.append([i, hash[i]])

#         return ans

# times = int(input("enter any value of array"))
# arr = []
# for i in range(times):
#     temp = int(input("give no"))
#     arr.append(i)
# s1 = Solution()

# print(s1.countFrequencies(arr))


