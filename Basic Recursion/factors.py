# You are given an integer n. Return the value of n! or n factorial.
# Factorial of a number is the product of all positive integers less than or equal to that number.

# Example 1
# Input: n = 2
# Output: 2
# Explanation: 2! = 1 * 2 = 2.

class Solution:
    def factorial(self, n):
        if( n == 1):
            return 1

        return n * self.factorial(n - 1)

s1 = Solution()
print(s1.factorial(3))