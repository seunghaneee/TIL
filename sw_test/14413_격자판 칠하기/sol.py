import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int ,input().split())
    array = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M-1):
            if array[i][j] == '#' and array[i][j+1] == '#':
                print(f'#{tc} possible')
                break
            elif array[i][j] == '.' and array[i][j+1] == '.':
                print(f'#{tc} possible')
                break

