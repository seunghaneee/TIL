import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    normal_num = 0
    for i in range(1,N-1):
        if numbers[i-1] < numbers[i] < numbers[i+1]:
            normal_num += 1
        elif numbers[i-1] > numbers[i] > numbers[i+1]:
            normal_num += 1

    print(f'#{tc} {normal_num}')
