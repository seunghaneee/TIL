import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    avg = sum(numbers) / len(numbers)

    count = 0
    for i in numbers:
        if i <= avg:
            count += 1

    print(f'#{tc} {count}')