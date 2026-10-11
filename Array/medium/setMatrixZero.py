# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
class Solution:

    # shreyash  Time: \(O(nm + z(n+m))\)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        i_index = []
        j_index = []

        for i in range(0 , n):
            for j in range(0 , m):
                if(matrix[i][j] == 0):
                    i_index.append(i)
                    j_index.append(j)

        for i in range(len(i_index)):
            # row values
            for j in range(0 , m):
                matrix[i_index[i]][j] = 0

            # colum value
            for j in range(0 , n):
                matrix[j][j_index[i]] = 0


    #shreyah gpt   
   
    def setZeroesOptimize(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        isRowZero = False
        isColumnZero = False

        # Step 1: Check if the first row contains zero
        for j in range(m):
            if matrix[0][j] == 0:
                isRowZero = True
                break

        # Check if the first column contains zero
        for i in range(n):
            if matrix[i][0] == 0:
                isColumnZero = True
                break

        # Step 2: Mark rows and columns
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set marked rows to zero
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0

        # Step 4: Set marked columns to zero
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0

        # Step 5: Handle the first row
        if isRowZero:
            for j in range(m):
                matrix[0][j] = 0

        # Step 6: Handle the first column
        if isColumnZero:
            for i in range(n):
                matrix[i][0] = 0