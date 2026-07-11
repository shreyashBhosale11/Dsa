# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        def helper(left, right):
            if left >= right:
                return True

            if cleaned[left] != cleaned[right]:
                return False

            return helper(left + 1, right - 1)

        return helper(0, len(cleaned) - 1)
    

            # optimize solution 
    def Chatgpt(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    
    # striver

    def striver(self, s: str) -> bool:
        
        chars= []
        for ch in s:
    
            if ch.isalnum():
                chars.append(ch.lower())
        cleaned = "".join(chars)
        n = len(cleaned)


        def help(i):
            if i >=  n // 2:
                return True

            if cleaned[i] != cleaned[n - i - 1]:
                return False

            return help(i + 1)

        return help(0)

s1 = Solution()

word = "madam is "
print(s1.striver(word))
        


        



