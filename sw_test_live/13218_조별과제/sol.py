import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    if N > 2:
        result = N // 3
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {result}')