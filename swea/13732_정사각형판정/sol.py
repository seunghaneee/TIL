import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # #인 부분 좌표로 받아오기
    list_a = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                list_a. append([i, j])
    print(list_a)

    leng_x = (list_a[-1][1] - list_a[0][1]) + 1
    leng_y = (list_a[-1][0] - list_a[0][0]) + 1
    list_b = []
    if leng_x - leng_y == 0:
        for i in range(list_a[0][0], list_a[-1][0] + 1):
            for j in range(list_a[0][1], list_a[-1][1] + 1):
                if arr[i][j] == '#':
                    list_b.append(arr[i][j])
    if list_b == ['#'] * leng_x * leng_y:
        result = 'yes'
    else:
        result = 'no'
    print(leng_x)
    print(f'#{tc} {result}')