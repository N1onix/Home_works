mass = [1, 3, 4, 56, 7, 8, 1, 2, 3, 2]
sum = 0
max = 0
min = 10000
index = 0
index_1 = 0
for i in range(len(mass)):
    if mass[i] > max:
        max = mass[i]
        index = i

for i in range(len(mass)):
    if mass[i] <= min:
        min = mass[i]
        index_1 = i

if index_1 != 0 and index_1 != len(mass) - 1:
    sum += (mass[index_1 - 1] + mass[index_1 + 1])
elif index_1 == len(mass) - 1:
    sum += mass[index_1 - 1]
else:
    sum += mass[index_1 + 1]

if index != 0 and index != len(mass) - 1:
    sum += (mass[index - 1] + mass[index + 1])
elif index_1 == len(mass) - 1:
    sum += mass[index_1 - 1]
else:
    sum += mass[index + 1]

print(sum)


