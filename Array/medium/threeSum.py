# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.



class Solution:

    # shreysh bruteForce
    def threeSumBruteForce(self, nums: list[int]) -> list[list[int]]:
        triple = []
       
        for i in range(len(nums)):
            for j in range(i + 1 ,len(nums)):
                for k in range(j + 1 , len(nums)):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        one_triple = [nums[i] , nums[j] , nums[k]]
                        

                        # Avoid duplicate triplets
                        one_triple.sort()
                        if one_triple not in triple:
                            triple.append(one_triple)

        return triple


# chatgpt Time: \(O(n^2)\) Auxiliary space: \(O(\log n)\)
    def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
s1 = Solution()
num = s1.threeSum(nums)
print(num)
