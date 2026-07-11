# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
# Example 1
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0 
        while(x != 0):
            digit = x % 10 
            rev = rev * 10 + digit
            x //= 10
        
        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev

s1 = Solution()

print(s1.reverse(1234))
print(s1.reverse(-345))
print(s1.reverse(-34566556))

    