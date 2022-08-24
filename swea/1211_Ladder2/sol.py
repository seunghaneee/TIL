import sys
sys.stdin = open('input.txt')

T = 10
# 좌 우 하 이동
dx = [0, 0, 1]
dy = [-1, 1, 0]
for tc in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    # 시작 지점이 1인 지점 찾기
    start = []
    for i in range(100):
        if array[0][i] == 1:
            start.append(i)

    # 시작 지점
    max_count = 0
    for i in start:
        r = 0
        c = i
        idx = 0
        count = 0
        while r != 99:
            temp_r = r + dx[idx]
            temp_c = c + dy[idx]
            if 0 <= temp_c < 100:
                if array[temp_r][temp_c] == 1:
                    r = temp_r
                    c = temp_c
                    array[temp_r][temp_c] = -1
                    count += 1
            idx = (idx + 1) % 3
        if max_count < count:
            max_count = count

    print(max_count)




