import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    result = []
    result.append(a//b)
    result.append(a%b)
    print(f'#{tc}', *result)