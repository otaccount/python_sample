N, M = map(int, input().split())
AN = list(map(int, input().split()))
BM = list(map(int, input().split()))

C = AN + BM
C.sort()

ANS_A = [0]*len(AN)
ANS_B = [0]*len(BM)

CNT_A = 0
CNT_B = 0
for idx_i, i in enumerate(C):
    for idx_a, a in enumerate(AN[CNT_A:], CNT_A):
        if i == a:
            ANS_A[idx_a] = idx_i+1
            CNT_A += 1
            break
    for idx_b, b in enumerate(BM[CNT_B:], CNT_B):
        if i == b:
            ANS_B[idx_b] = idx_i+1
            CNT_B += 1
            break

print(" ".join(map(str, ANS_A)))
print(" ".join(map(str, ANS_B)))
