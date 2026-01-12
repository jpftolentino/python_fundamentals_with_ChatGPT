# ================================
# 2D MATRIX PRACTICE PROBLEM SET
# Use for-loops and nested for-loops
# ================================


# --------------------------------
# Level 1: Warm-up (index comfort)
# --------------------------------

# 1) Print all elements row-major, one per line, as: r c value
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# 0 0 1
# 0 1 2
# 0 2 3
# 1 0 4
# 1 1 5
# 1 2 6

# row = len(mat)
# col = len(mat[0])

# for r in range(row):
#     for c in range(col):
#         print(r, c, mat[r][c])

# 2) Print all elements column-major, one per line, as: r c value
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# 0 0 1
# 1 0 4
# 0 1 2
# 1 1 5
# 0 2 3
# 1 2 6

# row = len(mat)
# col = len(mat[0])

# for c in range(col):
#     for r in range(row):
#         print(r, c, mat[r][c])

# 3) Compute the sum of each row and return a list
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# [6, 15]

# def sum_each_row(mat: list[int]) -> list[int]:
#     row = len(mat)
#     col = len(mat[0])
#     sum = []

#     for r in range(row):
#         temp_sum = 0
#         for c in range(col):
#             temp_sum += mat[r][c]
#         sum.append(temp_sum)

#     return sum

# print(sum_each_row(mat))


# 4) Compute the sum of each column and return a list
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# [5, 7, 9]

# def sum_each_col(mat: list[int]) -> list[int]:
#     row = len(mat)
#     col = len(mat[0])
#     sum = []
    
#     for c in range(col):
#         curr_sum = 0
#         for r in range(row):
#             curr_sum += mat[r][c]
#         sum.append(curr_sum)    
    
#     return sum

# print(sum_each_col(mat))


# 5) Find the max element and return (value, r, c)
# Sample input:
# mat = [
#     [3, 1, 4],
#     [1, 5, 9],
# ]
# Sample output:
# (9, 1, 2)

# def find_max(mat: list[int]) -> list:
#     row = len(mat)
#     col = len(mat[0])
#     max = [float("-inf"), 0, 0]
    
#     for r in range(row):
#         for c in range(col):
#             if mat[r][c] > max[0]:
#                 max[0] = mat[r][c]
#                 max[1] = r
#                 max[2] = c

#     return max[0], max[1], max[2]


# print(find_max(mat))

# 6) Count how many elements are even
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# 3

# def count_even(mat: list[int]) -> list:
#     row = len(mat)
#     col = len(mat[0])
#     even_count = 0

#     for r in range(row):
#         for c in range(col):
#             if mat[r][c] % 2 == 0:
#                 even_count += 1

#     return even_count

# print(count_even(mat))

# --------------------------------
# Level 2: Build outputs
# --------------------------------

# 7) Create a new matrix where every element is doubled
# Sample input:
mat = [
    [1, 2],
    [3, 4],
]
# Sample output:
# [
#     [2, 4],
#     [6, 8],
# ]

def mat_double(mat: list[int]) -> list[int]:
    rows = len(mat)
    cols = len(mat[0])
    new_mat = []

    for r in range(rows):
        row = []
        for c in range(cols):
            doubled = mat[r][c] * 2
            row.append(doubled)
        new_mat.append(row)

    return new_mat

print(mat_double(mat))


# 8) Create a new matrix where out[r][c] = r + c
# Same shape as input
# Sample input:
# mat = [
#     [0, 0, 0],
#     [0, 0, 0],
# ]
# Sample output:
# [
#     [0, 1, 2],
#     [1, 2, 3],
# ]


# 9) Transpose a matrix (rows become columns)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# [
#     [1, 4],
#     [2, 5],
#     [3, 6],
# ]


# 10) Reverse each row (mirror left to right)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
# Sample output:
# [
#     [3, 2, 1],
#     [6, 5, 4],
# ]


# 11) Reverse the order of rows (flip top to bottom)
# Sample input:
# mat = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
# Sample output:
# [
#     [5, 6],
#     [3, 4],
#     [1, 2],
# ]


# 12) Create a checkerboard matrix of 0s and 1s
# Use (r + c) % 2
# Sample input:
# mat = [
#     [0, 0, 0],
#     [0, 0, 0],
# ]
# Sample output:
# [
#     [0, 1, 0],
#     [1, 0, 1],
# ]


# --------------------------------
# Level 3: Traversal challenges
# --------------------------------

# 13) Print matrix in snake rows
# Even rows: left to right
# Odd rows: right to left
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# 1 2 3 6 5 4 7 8 9


# 14) Print matrix in snake columns
# Even columns: top to bottom
# Odd columns: bottom to top
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# 1 4 7 8 5 2 3 6 9


# 15) Collect main diagonal and anti-diagonal (square matrix)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# main = [1, 5, 9]
# anti = [3, 5, 7]


# 16) Sum elements above the main diagonal (square matrix)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# 11   # (2 + 3 + 6)


# 17) Sum the border elements (no double-counting corners)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# 40


# --------------------------------
# Level 4: Rotations (square matrices)
# --------------------------------

# 18) Rotate 90 degrees clockwise (new matrix)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3],
# ]


# 19) Rotate 90 degrees counter-clockwise (new matrix)
# Sample output:
# [
#     [3, 6, 9],
#     [2, 5, 8],
#     [1, 4, 7],
# ]


# 20) Rotate 180 degrees (new matrix)
# Sample output:
# [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1],
# ]


# 21) Rotate 90 degrees clockwise IN-PLACE
# No extra matrix allowed
# Sample input/output same as problem 18


# 22) Rotate 90 degrees clockwise four times
# Check if the matrix returns to original
# Sample input:
# mat = [
#     [1, 2],
#     [3, 4],
# ]
# Sample output:
# True


# --------------------------------
# Level 5: Advanced traversal
# --------------------------------

# 23) Print elements in spiral order (clockwise)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# 1 2 3 6 9 8 7 4 5


# 24) Compute the sum of each ring (outer to inner)
# Sample input:
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Sample output:
# [40, 5]


# 25) For each cell, count valid neighbors (up/down/left/right)
# Sample input:
# mat = [
#     [0, 0],
#     [0, 0],
# ]
# Sample output:
# [
#     [2, 2],
#     [2, 2],
# ]


# 26) For each cell, sum its neighbors (up/down/left/right)
# Missing neighbors count as 0
# Sample input:
# mat = [
#     [1, 2],
#     [3, 4],
# ]
# Sample output:
# [
#     [5, 5],
#     [5, 5],
# ]


# 27) Longest strictly increasing path moving only right or down
# Return the length
# Sample input:
# mat = [
#     [1, 2, 3],
#     [2, 3, 4],
# ]
# Sample output:
# 4
