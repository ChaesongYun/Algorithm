import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    _ = input()
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    ci = 99
    for i in range(102):
        if arr[ci][i] == 2:
            cj = i
    while ci > 0:
        arr[ci][cj] = 0
        if arr[ci][cj + 1] == 1:
            cj += 1
        elif arr[ci][cj - 1] == 1:
            cj -= 1
        else:
            ci -= 1
    print(f"#{tc} {cj-1}")