# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

# Example 1
# Input: n1 = 4, n2 = 6
# Output: 2
# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
# Greatest Common divisor = 2.

class Solution:
    def GCD1(self, n1, n2):
        num = min(n1 , n2)
        bigValue = 0
        for i in range(num , 0 , -1):
            if(n1 % i == 0 and n2 % i == 0):
                return i


    # euclidean algorithm   

    def GCD2(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1 % n2

        return n1
    


    # leetcode problem 
    def findGCD(self, nums: List[int]) -> int:
        smallest = largest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num
            elif num > largest:
                largest = num

        while largest != 0:
            smallest, largest = largest, smallest % largest

        return smallest
            
    
s1 = Solution()
print(s1.GCD1(4 , 6))
print(s1.GCD2(4 , 6))

