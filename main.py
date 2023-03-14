
if __name__ == '__main__':
    N = int(input())
    N1, N2 = map(int, input().split())
    NLIST = list(map(int, input().split()))

    print(f"1行目:{N}")
    print(f"2行目合計:{N1+N2}")
    print(f"3行目合計:{sum(NLIST)}")