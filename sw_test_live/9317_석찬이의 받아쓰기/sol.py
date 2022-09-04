import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = list(input())
    seok = list(input())

    count = 0
    for i in range(N):
        if answer[i] != seok[i]:
            count+=1
    # print(count)
    result = N - count
    print(f'#{tc} {result}')