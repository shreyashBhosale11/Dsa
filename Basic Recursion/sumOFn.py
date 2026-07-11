# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

# Example 1
# Input : N = 4
# Output : 10
# Explanation : first four natural numbers are 1, 2, 3, 4.
# Sum is 1 + 2 + 3 + 4 => 10.

class Solution:
    def NnumbersSum(self, n):
        
        if(n == 0):
            return 0

        return n + self.NnumbersSum( n - 1)
    

    def StriversSum(self, n, total):
        if n == 0:
            print(total)
            return

        self.NnumbersSum(n - 1, total + n)

        
        

s1 = Solution()
print(s1.NnumbersSum(4))