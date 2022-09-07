import sys
sys.stdin = open('input1.txt')
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 전치행렬
    arr_T = list(map(list, zip(*arr)))
    max_a = 0

    # 가로 방향 확인
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            else:
                max_a = max(max_a, count)
                count = 0
        max_a = max(max_a, count)

    for i in range(M):
        count_T = 0
        for j in range(N):
            if arr_T[i][j] == 1:
                count_T += 1
            else:
                max_a = max(max_a, count_T)
                count_T = 0
        max_a = max(max_a, count_T)


    print(f'#{test_case} {max_a}')