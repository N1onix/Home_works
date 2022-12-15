# (x&41 ≠ 0) → ((x&33 = 0) → (x&А ≠ 0))
for A in range(64):
    flag = True
    for x in range(64):
        if not((x & 41 != 0) <= ((x & 33 == 0) <= (x & A != 0))):
            flag = False
    if flag:
        print(A)
        break