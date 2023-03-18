# practice_a
# 積が偶数か奇数かを判定
a, b = map(int, input().split())

multi = a * b
if multi % 2 == 0:
    print("Even")
else:
    print("Odd")