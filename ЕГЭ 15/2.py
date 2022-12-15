# ДЕЛ(A, 45) ∧ (ДЕЛ(750, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not((A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))):
            flag = False
    if flag:
        print(A)
        break