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

sum = 0
max_sum = 0
min_sum = 100000
index_max_sum = 0
index_min_sum = 0
for x in range(len(new_matrix)):
    for y in range(len(new_matrix)):
        sum += new_matrix[x][y]
    if sum < min_sum:
        min_sum = sum
        index_min_sum = x
    if sum >= max_sum:
        max_sum = sum
        index_max_sum = x
    sum = 0
a = new_matrix[index_min_sum]
b = new_matrix[index_max_sum]
new_matrix[index_min_sum] = b
new_matrix[index_max_sum] = a
print(sum, min_sum, max_sum, index_min_sum, index_max_sum)
print(new_matrix)