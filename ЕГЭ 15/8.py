# (ДЕЛ(x, 3) → ¬ДЕЛ(x, 5)) ∨ (x + A ≥ 90)
for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if not(((x % 3 == 0) <= (x % 5 != 0)) or (x + A >= 90)):
            flag = False
    if flag:
        print(A)
        break
