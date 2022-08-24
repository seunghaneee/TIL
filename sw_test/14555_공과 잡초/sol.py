import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()

    # 공이 될 수 있는 조건
    # (), |), (|
    count = 0
    for i in range(len(N)-1):
        if N[i] == '(':
            if N[i+1] == ')' or N[i+1] == '|':
                count += 1
        elif N[i] == '|' and N[i+1] == ')':
            count += 1

    print(f'#{tc} {count}')