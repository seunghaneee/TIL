import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    abs_sum = []
    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            total = 0
            for idx in range(4):
                ni = i + dx[idx]
                nj = j + dy[idx]
                if 0 <= ni < N and 0 <= nj < N:
                    a = abs(point - arr[ni][nj])
                    total += a
            abs_sum.append(total)

    print(f'#{tc} {sum(abs_sum)}')

