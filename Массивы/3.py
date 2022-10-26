mass = [1, 3, 4, 56, 7, 8, 1, 2, 3, 2]
index = 0
index_1 = 0
sum = 0
for i in range(len(mass)):
    if mass[i] // 2:
        index = i
    if mass[i] % 2:
        index_1 = i

if index != 0 and index != len(mass) - 1:
    sum += (mass[index - 1] + mass[index + 1])
elif index == len(mass) - 1:
    sum += mass[index - 1]
else:
    sum += mass[index + 1]

if index_1 != 0 and index_1 != len(mass) - 1:
    sum += (mass[index_1 - 1] + mass[index_1 + 1])
elif index_1 == len(mass) - 1:
    sum += mass[index_1 - 1]
else:
    sum += mass[index_1 + 1]

print(sum)

