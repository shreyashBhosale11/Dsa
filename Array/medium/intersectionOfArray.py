# Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays; that is, if an element appears x times in nums1 and y times in nums2, it should appear min(x, y) times in the result.

# The intersection of two arrays is an array where all values are present in both arrays.

# Example 1:
# Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]

# Output: [1, 2]

# Explanation:

# The elements 1, 2 are the only elements present in both nums1 and nums2

# Example 2:


class Solution:

    # shreyash bruteforce 
    def intersectionOfArray(self , num1 , num2):
        arr = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                if(num1[i]== num2[j]):
                    arr.append(num1[i])
                    break

        return arr


    # shreyash optmize 
    def intersectionOfArrayOptimize(self , num1 , num2):
        i = 0 
        j = 0
        arr = []
        while(i < len(num1) and j < len(num2)):
            if(num1[i] == num2[j]):
                arr.append(num1[i])
                i +=1
                j +=1
            else:
                if(num1[i] < num2[j]):
                    i += 1
                else:
                    j += 1


        return arr


