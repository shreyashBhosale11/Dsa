# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.

# Example 1
# Input: n = 5
# Output: true
# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        
        for i in range(2 , int(n ** 0.5) + 1) :
            if(n % i == 0):
                return False
                
        return True
        

s1 = Solution()
print(s1.isPrime(5))
print(s1.isPrime(8))