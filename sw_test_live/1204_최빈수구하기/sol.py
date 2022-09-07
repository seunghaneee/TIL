import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    C = [0] * 101
    for i in numbers:
        C[i] += 1

    max_result = max(C)
    idx_num = 0
    for i in range(len(C)-1, -1, -1):
        if C[i] == max_result:
            idx_num = i
            break

    print(f'#{tc} {idx_num}')