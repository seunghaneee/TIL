import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 중간 인덱스
    mid = N//2

    start = end = mid
    total = 0

    for i in range(N):
        for j in range(start, end+1):
            total += arr[i][j]

        if i < mid:
            # 아직 행 인덱스(i)가 중간까지 안왔으면 양쪽으로 한칸씩 더 벌려서 더한다.
            start -= 1
            end += 1
        elif i >= mid:
            start += 1
            end -= 1
    print(f'#{tc} {total}')
