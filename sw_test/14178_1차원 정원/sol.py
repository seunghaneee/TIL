import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())

    # D에 따른 커버할 수 있는 넓이는 2D + 1 이다.
    if N == 1:
        total = 1
    if  N % (2*D + 1) == 0:
        total = N // (2*D + 1)

    else:
        total = N // (2*D + 1) + 1

    print(f'#{tc} {total}')