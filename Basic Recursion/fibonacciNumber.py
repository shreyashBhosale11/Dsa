# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        return self.fib(n - 1) + self.fib(n- 2)
    

    # top down Dp 
    def fibOPtimize(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = solve(n - 1) + solve(n - 2)
            return memo[n]

        return solve(n)
    
    # Tabulation (Bottom-Up DP) 
    def fibThirdChatgpt(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    

    # most optimize  without resursion 
    def fibOPtimize(self, n: int) -> int:
        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1
