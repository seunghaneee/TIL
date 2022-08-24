import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    num_list = list(str(num))
    num_list.sort()
    # print(num_list)
    # num의 각 자리수를 적절히 조정하여 N보다 큰 N의 배수가 되도록 설정

    new_num = num
    i = 2
    while new_num < 10**6:
        new_num = num * i
        new_num_list = list(str(new_num))
        i += 1
        new_num_list.sort()
        if num_list == new_num_list:
            print(f'#{tc} possible')
            break
    if num_list != new_num_list:
        print(f'#{tc} impossible')

