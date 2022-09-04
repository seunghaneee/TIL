import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                result = i * j
                break
        if result == N:
            break

    if result > 0:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
