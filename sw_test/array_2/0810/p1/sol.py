import sys
sys.stdin = open('input.txt')

T = int(input())
# 상 하 좌 우
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    idx = 0
    result = 0

    for r in range(N):
        for c in range(N):
            for idx in range(4):
                temp_r = r + dx[idx]
                temp_c = c + dy[idx]

                if 0 <= temp_c < N and 0 <= temp_r < N:
                    result += abs(array[temp_r][temp_c] - array[r][c])

    print(result)


