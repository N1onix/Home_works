# x & 73 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
for A in range(128):
    flag = True
    for x in range(128):
        if not((x & 73 == 0) <= ((x & 28 != 0) <= (x & A != 0))):
            flag = False
    if flag:
        print(A)
        break