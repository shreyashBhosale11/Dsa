# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:

    # shreyash optimize 
    def generate(self, numRows: int) -> list[list[int]]:
        arr: list[list[int]] = []

        for i in range(numRows):
            row = []
            row.append(1)

            if(i > 1):
                for j in range(1, i):
                    row.append(arr[i-1][j-1] + arr[i-1][j])

            if i > 0 :
                row.append(1)
                
            arr.append(row)

        return arr


s1 = Solution()

arr1 = s1.generate(5)
print(arr1)

