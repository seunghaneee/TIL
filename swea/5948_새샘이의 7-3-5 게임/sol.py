import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    sum_ilst = []

    for i in range(len(numbers)-2):
        for j in range(i+1, len(numbers)-1):
            for k in range(j+1, len(numbers)):
                sum_ilst.append(numbers[i] + numbers[j] + numbers[k])

    new_list = sorted(set(sum_ilst))
    print(f'#{tc}', new_list[-5])