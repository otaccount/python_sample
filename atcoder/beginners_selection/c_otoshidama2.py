N, Y = map(int, input().split())
anum, bnum, cnum = -1, -1, -1

for a in range(N+1):
    for b in range(N+1):
        c = N - a - b

        if c < 0 or c > N:
            continue

        if 10000 * a + 5000 * b + 1000 * c == Y:
            anum, bnum, cnum = a, b, c

print(anum, bnum, cnum)

def ng2():
    N, Y = map(int, input().split())
    anum, bnum, cnum = -1, -1, -1

    for a in range(N + 1):
        for b in range(N + 1):
            for c in range(N + 1):
                if a + b + c == N and \
                        a * 10000 + b * 5000 + c * 1000 == Y:
                    anum = a
                    bnum = b
                    cnum = c

    print(f"{anum} {bnum} {cnum}")
def ng1():
    N, Y = map(int, input().split())
    num_1 = 0
    num_2 = 0
    num_3 = 0

    num_1 = int(Y / 10000)
    amari = Y % 10000
    print(amari)

    num_2 = int(amari / 5000)
    amari = amari % 5000

    num_3 = int(amari / 1000)
    amari = amari % 1000

    if amari == 0:
        print(f"{num_1} {num_2} {num_3}")
    else:
        print("-1 - 1 -1")