# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.

# Example 1
# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6

class Solution:
    def divisors(self, n):
        arr= []
        index = 0
        for i in range(1 , n+1):
            if(n % i == 0):
                n = n// i
                arr.append(i)
                if i != n // i:
                    arr.append(n // i)
        arr.sort()
        return arr

s1 = Solution()
print(s1.divisors(7))
print(s1.divisors(36))
print(s1.divisors(12))

