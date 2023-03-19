N, M = map(int, input().split())
AN = list(map(int, input().split()))
BM = list(map(int, input().split()))

AN_IDX = 0
AN_ANS = []
BM_IDX = 0
BM_ANS = []
C_IDX = 0
#while True:
for i in AN[AN_IDX:]:
    for j in BM[BM_IDX:]:
        if i < j:
            AN_ANS.append(C_IDX+1)
            AN_IDX += 1
            C_IDX += 1
            break
        else:
            BM_IDX += 1
            BM_ANS.append(C_IDX+1)
        C_IDX += 1

for i in AN[AN_IDX:]:
    AN_ANS.append(C_IDX+1)
    C_IDX += 1

for i in BM[BM_IDX:]:
    BM_ANS.append(C_IDX+1)
    C_IDX += 1

print(" ".join(map(str, AN_ANS)))
print(" ".join(map(str, BM_ANS)))
