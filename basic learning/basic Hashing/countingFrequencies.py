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

class Solution:
    # arrayHashing tecquique 
    def countFrequencies(self, nums):
        # Your code goes here
        max = 0
        for num in nums:
            max = max(max , num)        
        hash = [0]* max

        for i in range(len(nums)):
            hash[i] += 1

        return hash 

    # dic hashing 
    def dicCountFrequencies(self, nums):
        hashmap ={}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1

        # for i in range(len(nums)):
        #     if(nums[i] in hashmap):
        #         hashmap[nums[i]] += 1
        #     else:
        #         hashmap[nums[i]] = 1
        return hashmap

    def maxmum(self , arr):
        hashmap =self.dicCountFrequencies(arr)
        max_element = None
        max_frequency = 0

        for key, value in hashmap.items():
            if value > max_frequency:
                max_frequency = value
                max_element = key

        print(max_element, max_frequency)
            


   


arr = [1, 2, 2, 1 , 3]

s1 = Solution()
nums1 = s1.dicCountFrequencies(arr)
print(nums1)

s1.maxmum(arr)



    
