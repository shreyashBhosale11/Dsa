# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

# Example 1
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# Output: [1, 2, 3, 4, 5, 7]
# Explanation:
# # The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums

class Solution:
    def unionArray(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)

        i = 0
        j = 0

        ans = []

        while i < l1 and j < l2:

            if nums1[i] <= nums2[j]:
                if len(ans) == 0 or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1

            else:
                if len(ans) == 0 or ans[-1] != nums2[j]:
                    ans.append(nums2[j])
                j += 1


        while i < l1:
            if len(ans) == 0 or ans[-1] != nums1[i]:
                ans.append(nums1[i])
            i += 1


        while j < l2:
            if len(ans) == 0 or ans[-1] != nums2[j]:
                ans.append(nums2[j])
            j += 1


        return ans


arr1 = [1 , 2, 3, 4, 5, ]
arr2 = [1 , 2,7 ]


s1 = Solution()

num2 = s1.unionArray(arr1 , arr2)

print("largest number is " , num2  )


