# 61. Pascal's Triangle I
# Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.

# In Pascal's triangle:

# The first row contains a single element 1.
# Each row has one more element than the previous row.
# Every row starts and ends with 1.
# For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

# Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
# where indexing is 1-based
# Example 1:
# Input: r = 4, c = 2

# Output: 3

# Explanation:

# The Pascal's Triangle is as follows:


# GPT
def pascalTriangle(self, r: int, c: int) -> int:
    n = r - 1
    k = c - 1

    result = 1

    for i in range(k):
        result = result * (n - i) // (i + 1)

    return result
