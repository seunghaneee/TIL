import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N 행 / M 열
    N, M = map(int, input().split())
    array = [list(map(str, input())) for _ in range(N)]
    # print(array)
    # 바꿔야 되는 색의 최대값은 전체칸 다 새로 색칠할 때
    result = N*M
    # 하얀색은 1줄만 있는 경우 ~ 마지막 2줄 빼고 다 있는 경우
    W_count = 0
    for white in range(N-2):
        for col in range(M):
            if array[white][col] != 'W':
                W_count += 1
        # 파란색은 하얀줄 다음 행부터 올 수 있다.
        # 최소한 마지막 한줄은 빨간색을 위한 줄을남겨야 한다.
        B_count = 0
        for blue in range(white+1, N-1):
            for col in range(M):
                if array[blue][col] != 'B':
                   B_count += 1
            R_count = 0
            for red in range(blue+1, N):
                for col in range(M):
                    if array[red][col] != 'R':
                        R_count += 1

            count = W_count + B_count + R_count

            # 최소값 찾기
            if result > count:
                result = count

    print(f'#{tc} {result}')