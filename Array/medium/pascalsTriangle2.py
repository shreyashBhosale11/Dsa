# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

class Solution:

    # shreyash 
    def getRow(self, rowIndex: int) -> list[int]:
        arr = []

        for i in range(rowIndex + 1):
            row = []
            row.append(1)

            if( i > 1):
                for j in range(1 , i):
                    row.append(arr[i-1][j-1] + arr[i-1][j])

            if(i > 0):
                row.append(1)
            if(i == rowIndex):
                return row
            arr.append(row)


    # optimize chat gpt 
    def getRowOptimize(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for i in range(1 ,rowIndex + 1):
            row.append(1)

            for j in range(i-1 , 0 , -1):
                row[j] = row[j] + row[j-1]         

        return row 
            
