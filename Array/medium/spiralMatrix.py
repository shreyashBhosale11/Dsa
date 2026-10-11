class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

        arr =[ [0] *  n for _ in range(n)]
        number = 1

        left = 0
        right = n-1
        top = 0 
        bottom = n-1

        while number <= n * n :
            for i in range(left , right + 1 ):
                arr[top][i] = number
                number += 1

            top += 1
            for i in range(top , bottom + 1):
                arr[i][right] = number
                number += 1

            right -= 1
            for i in range(right , left -1 , -1):
                arr[bottom][i] = number
                number += 1

            bottom -= 1
            for i in range(bottom , top -1 , -1):
                arr[i][left] = number
                number += 1

            left += 1

        return arr