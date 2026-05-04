# Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
# A number ends with digit d if its last digit is d.
# Example 1
# Input: d = 1
# Output: 12300
# Explanation:
# The first 50 positive integers ending with 1 are: 1, 11, 21, 31, ..., 491
# Their sum is 12300.


class Solution:
    def whileLoop(self, d: int) -> int:
        count = 0
        num = d
        total = 0
        
        while count < 50:
            if num > 0:          
                total += num
                count += 1
            num += 10
        
        return total 

s1 = Solution()
num = 5
print(s1.whileLoop(5))
