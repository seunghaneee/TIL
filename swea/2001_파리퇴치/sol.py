import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N = 배열 크기, M = 파리채 크기
    N, M = map(int, input().split())
    # 파리 마리수 배열
    array = [list(map(int, input().split())) for _ in range(N)]

    # 합계 중 가장 큰 값을 저장할 result
    result = 0

    # 탐색 범위
    # N = 5, M = 2 일 때 N-M+1번 탐색 해야 한다.
    # -> N-M+1
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 파리채 범위만큼 확인
            total = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    total += array[x][y]
            # print(total)
            if total > result:
                result = total
    # print('============')
    print(f'#{tc} {result}')
