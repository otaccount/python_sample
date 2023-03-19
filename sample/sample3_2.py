N, M = map(int, input().split())
AN = list(map(int, input().split()))
BM = list(map(int, input().split()))

C = AN + BM
C.sort()

ANS_A = [0]*len(AN)
ANS_B = [0]*len(BM)

for idx_i, i in enumerate(C):
    if AN.__contains__(i):
        for idx_a, a in enumerate(AN):
            if i == a:
                ANS_A[idx_a] = idx_i+1
                break
    elif BM.__contains__(i):
        for idx_b, b in enumerate(BM):
            if i == b:
                ANS_B[idx_b] = idx_i+1
                break

print(" ".join(map(str, ANS_A)))
print(" ".join(map(str, ANS_B)))
