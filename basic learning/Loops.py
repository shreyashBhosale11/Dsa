# Given two integers low and high, return the sum of all integers from low to high inclusive.
# Example 1
# Input: low = 1, high = 5
# Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15

class Solution:
    def forLoop(self, low : int, high : int) -> int:
        total = 0
        for i in range(low , high + 1):
            total += i
        return total