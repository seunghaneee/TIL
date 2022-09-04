import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    if A + B <= N:
        min_number = 0
        max_number = min(A, B)
    elif A + B > N:
        min_number = A + B - N
        max_number = min(A, B)


    print(f'#{tc} {max_number} {min_number}')
