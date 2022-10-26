mass = [1, 3, 4, 56, 7, 8, 1, 1, 1, 1, 1, 1, 1, 1]
count = 1
for i in range(len(mass)):
    if i != len(mass) - 1 and mass[i] == mass[i + 1]:
        count += 1
print(count)