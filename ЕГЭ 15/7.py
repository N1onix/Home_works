# (x > A) ∨ (y > A) ∨ (2y + x < 110)
for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((x > A) or (y > A) or (2 * y + x < 110)):
                flag = False
                break
    if flag:
        print(A)
        