def func(matrix):
    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[rows][column] == 0:
                for i in range(len(matrix)):
                    matrix[i][column] = 0
                for i in range(len(matrix[0])):
                    matrix[rows][i] = 0

    return matrix


matrix = [[1, 2, 4], [5, 0, 7], [8, 9, 0]]
print(func(matrix))

"""'
1 2 4
5 0 7
8 9 0 

1,2
1,2 
"""

