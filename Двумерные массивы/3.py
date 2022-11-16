matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]
mass = []
new_matrix = []
for j in range(3):
    for i in range(3):
        mass.append(matrix[i][j])
    new_matrix.append(mass)
    mass = []
min = 100000
max = 0
index_max_simvola = 0
index_min_simvola = 0
for x in range(len(new_matrix)):
    for y in range(len(new_matrix)):

        if new_matrix[x][y] <= min:
            min = new_matrix[x][y]
            index_min_simvola = x
        if new_matrix[x][y] > max:
            max = new_matrix[x][y]
            index_max_simvola = x

a = new_matrix[index_min_simvola]
b = new_matrix[index_max_simvola]
new_matrix[index_min_simvola] = b
new_matrix[index_max_simvola] = a
print(min, max, index_min_simvola, index_max_simvola)
print(new_matrix)