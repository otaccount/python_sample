N = int(input())
AN = list(map(int, input().split()))

for i in AN:
    if i % 2 == 0:
        print(i, end=" ")

print("")