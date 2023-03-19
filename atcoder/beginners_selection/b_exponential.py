X = int(input())

b, p = 1, 1
ans = 1
for i in range(1, X):
    for p in range(2, X):
        calc = i ** p

        if calc > X:
            break
        else:
            if ans < calc:
                ans = calc

print(ans)