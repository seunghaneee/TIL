import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    leng = int(input())

    result = 'Bob'
    a = leng - 1
    if a % 2 == 1:
        result = 'Alice'

    print(f'#{tc} {result}')