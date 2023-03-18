N = int(input())
NLIST = list(map(int, input().split()))

cnt = 0

while True:
    loopFlg = True
    for i_idx, i in enumerate(NLIST):
        if i % 2 == 1:
            loopFlg = False
            break
        else:
            NLIST[i_idx] = i / 2

    if not loopFlg:
        break
    cnt += 1

print(cnt)