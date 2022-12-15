# (2x + 3y > 30) ∨ (x + y ≤ A)
A = 1
for A in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            if not(((2 * x + 3 * y) > 30) or ((x + y) <= A)):
                flag = False
                break
    if flag:
        print(A)
        break