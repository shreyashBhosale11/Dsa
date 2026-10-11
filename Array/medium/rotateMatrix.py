# Description
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions


# Code
# Testcase
# Testcase
# Test Result
# 48. Rotate Image
# Medium
# Topics
# premium lock icon
# Companies
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


class Solution:

    # shreyah worng approch 
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)  #row
        m = len(matrix[0]) #colums
    
      
      

        rotation = m


        for i in range(1 , rotation):

            left = 0
            right = m-1
            top = 0
            down = n -1
            
            
            place = matrix[0][0]
            while(left <= right and top <= down):
                for i in range(left , right + 1):
                    temp = matrix[top][i]
                    matrix[top][i] = place
                    place = temp
                top += 1

                for i in range(top , down + 1):
                    temp = matrix[i][right]
                    matrix[i][right] = place
                    place = temp
                right -= 1

                for i in range(right , left -1 , -1):
                    temp = matrix[down][i]
                    matrix[down][i] = place
                    place = temp 
                down -= 1

                for i in range(down , top -1 , -1):
                    temp = matrix[i][left]
                    matrix[i][left] = place
                    place = temp
                left += 1


    # optimize gpt 
    def rotateOptimize(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(0 , n):
            for j in range (i + 1 , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        for row in matrix:
            row.reverse()
        

s1 = Solution()

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

s1.rotateOptimize(matrix)

print(matrix)
        
