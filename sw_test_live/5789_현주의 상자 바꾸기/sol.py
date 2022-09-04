import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box_list = [0] * N
    for i in range(1, Q+1):
        start, end = map(int, input().split())
        for j in range(start-1, end):
            box_list[j] = i

    print(f'#{tc}', *box_list)
