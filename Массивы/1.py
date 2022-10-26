mass = [1, 3, 4, 56, 7, 8, 1, 2, 3, 2]
min = 10000
index = 0
for i in range(len(mass)):
    if mass[i] <= min:
        min = mass[i]
        index = i
print(index)
