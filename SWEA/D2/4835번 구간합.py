import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mx = 0
    mn = 99999999
    for i in range(N-M+1):
        sm = 0
        for j in range(i, i+M):
            sm += lst[j]
        if sm < mn:
            mn = sm
        if sm > mx:
            mx = sm
    print(f"#{tc} {mx-mn}")