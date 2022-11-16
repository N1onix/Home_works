matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mass = []
new_matrix = []
for j in range(3):
    for i in range(3):
        mass.append(matrix[i][j])
    new_matrix.append(mass)
    mass = []
print(new_matrix)

