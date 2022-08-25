import sys
sys.stdin = open('sample_input(1).txt')
from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # 열우선탐색
    for j in range(1,N+1):
        for i in range(1, N+1):
            # 초기 설정
            if j == (N // 2) -1 and i == (N // 2) -1:
                arr[i][j] = 'W'
                arr[i+1][j] = 'B'
                arr[i][j+1] = 'B'
                arr[i+1][j+1] = 'W'

    for _ in range(M):
        y, x, col = map(int, input().split())
        if col == 1:  # 흑돌 1
            arr[y-1][x-1] = 'B'
        elif col == 2:  # 백돌 2
            arr[y-1][x-1] = 'W'

        # 행 계산
        # 왼쪽에서 가면서 처음 흑 만나고 오른쪽에서 왼쪽으로 가면서 처음 흑 만나면 그 가운데 전부 흑
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'B' and arr[i][N-j]


    print(arr)

