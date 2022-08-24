import sys
sys.stdin = open('input.txt')

T = 10
# 좌우상
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    for i in range(100):
        if array[r][i] == 2:
            # 도착 해야 하는 열의 인덱스
            final = i
            break

    # 도착지점에서 시작해서 올라간다.

    # 델타 이용
    idx = 0
    start = array[99][final]
    while r > 0:
        temp_r = r + dx[idx]    # 좌 우 움직임
        temp_c = final + dy[idx]    # 상 하 움직임
        # 범위 밖을 나가지 않게 설정
        if 0 <= temp_r < 100 and 0 <= temp_c < 100:
            if array[temp_r][temp_c] == 1:  # 현재 위치 기준 좌 우 상 확인하여 1이면
                # 내 위치를 1인 위치로 이동시키고
                r = temp_r
                final = temp_c
                # 내가 있던 위치는 숫자를 바꿔줌으로써 무한루프에 들어가지 않게 함
                array[temp_r][temp_c] = -1
        idx = (idx+1) % 4   # 계속 반복

    print(f'#{tc} {final}')
