import sys
sys.stdin = open('sample_input.txt')

T = int(input())
Time = [i for i in range(24)]
for tc in range(1, T+1):
    A, B = map(int, input().split())
    time = 0
    if A + B < 24:
        time = A + B
    elif A + B == 24:
        time = 0
    elif A + B > 24:
        time = A + B - 24

    print(f'#{tc} {time}')