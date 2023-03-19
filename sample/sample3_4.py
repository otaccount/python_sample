N, M = map(int, input().split())
AN = list(map(int, input().split()))
BM = list(map(int, input().split()))

C = AN + BM
C.sort()

ANS_A = [0]*len(AN)
ANS_B = [0]*len(BM)

CNT_A = 0
CNT_B = 0

for i in AN:
    print(C.index(i)+1, end=" ")
print("")
for i in BM:
    print(C.index(i)+1, end=" ")
print("")

