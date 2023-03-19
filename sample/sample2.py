H, W = map(int, input().split())
AHW = []
for i in range(H):
    AHW.append(list(map(int, input().split())))

for i in AHW:
    for j in i:
        if j == 0:
            print(".", end="")
        else:
            print(chr(64+j), end="")
    print("")

