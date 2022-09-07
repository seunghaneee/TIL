import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    total = 0

    # 1 ~ N 까지 숫자중 홀수는 더하고 짝수는 뺀다

    for i in range(1, N+1):
        if i % 2 != 0:
            total += i
        else:
            total -= i

    print(f'#{tc} {total}')