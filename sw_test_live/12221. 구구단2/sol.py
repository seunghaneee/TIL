import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = 0
    if 1 <= A < 10 and 1 <= B < 10:
        result = A * B
    elif (A >= 10) or (B >= 10):
        result = -1
    print(f'#{tc} {result}')