# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Example 1
# Input: n = 153
# Output: true
# Explanation: Number of digits : 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

class Solution:
    def isArmstrong(self, n):
        num1 = n      # original number
        temp = n      # used for counting digits
        num2 = 0
        digit = 0

        # Count digits
        while temp != 0:
            temp //= 10
            digit += 1

        temp = n      # reset temp

        # Calculate Armstrong sum
        while temp != 0:
            num2 += (temp % 10) ** digit
            temp //= 10

        return num1 == num2


s1 = Solution()
print(s1.isArmstrong(153))
