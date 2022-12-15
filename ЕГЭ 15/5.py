# P = [4, 15]
# Q = [12, 20]
# ((x ∈ P) ∧ (x ∈ Q)) → (x ∈ A)
p1, p2, q1, q2 = 4, 15, 12, 20

P = [i/10 for i in range(p1*10,p2*10 + 1)]
Q = [i/10 for i in range(q1*10,q2*10 + 1)]

def sol(x, A):
    return ((x in P) and (x in Q)) <= (x in A)
A = set()
for x in [i / 10 for i in range(3 * 10, 21 * 10 + 1)]:
    if not sol(x, A):
        A.add(x)
print(sorted(A))