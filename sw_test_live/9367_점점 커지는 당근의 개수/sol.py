import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    size_list = list(map(int, input().split()))

    count = 1
    max_leng = 1
    for i in range(len(size_list)-1):
        if size_list[i] < size_list[i+1]:
            count += 1
            if count > max_leng:
                max_leng = count
        else:
            count = 1

    print(f'#{tc} {max_leng}')