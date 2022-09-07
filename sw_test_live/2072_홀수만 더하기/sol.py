import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    number = list(map(int, input().split()))
    result = 0
    for i in number:
        if i % 2 != 0:
            result += i

    print(f'#{tc} {result}')