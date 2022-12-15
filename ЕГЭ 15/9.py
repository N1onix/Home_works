# ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
def sol(x, A):
    return ((x in A) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (x in A))
A = set([i/10 for i in range(-1000, 1000)])
for x in [i / 10 for i in range(-1000, 1000)]:
    if not sol(x, A):
        A.remove(x)
print(sorted(A))