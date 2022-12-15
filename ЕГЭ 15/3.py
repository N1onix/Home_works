# P = [2, 10]
# Q = [6, 14]
# ( (x ∈ А) → (x ∈ P) ) ∨ (x ∈ Q)
p1, p2, q1, q2 = 2, 10, 6, 14

P = [i/10 for i in range(p1*10,p2*10 + 1)]
Q = [i/10 for i in range(q1*10,q2*10 + 1)]

def sol(x, A):
    return ((x in A) <= (x in P)) or (x in Q)
A = set([i/10 for i in range(1 * 10, 20 * 10 + 1)])
for x in [i / 10 for i in range(1 * 10, 20 * 10 + 1)]:
    if not sol(x, A):
        A.remove(x)
print(sorted(A))
