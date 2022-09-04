import sys
sys.stdin = open('input.txt')
from pprint import pprint
T = 1
# 시계 회전 (상 우 하 좌)
dx1 = [-1, 0, 1, 0]
dy1 = [0, 1, 0, -1]

# 반시계 회전 (좌 하 우 상)
dx2 = [0, 1, 0, -1]
dy2 = [-1, 0, 1, 0]

for tc in range(1, T+1):
    # 가로X 세로Y 길이
    X, Y = map(int, input().split())
    # 상점 개수 N
    N = int(input())
    # [0]:1 북쪽 2 남쪽 3 서쪽 4 동쪽
    # [1]: 남, 북 일 경우 왼쪽경계부터 거리
    # [1]: 동, 서 일 경우 위쪽경계부터 거리
    shop_list = [list(map(int, input().split())) for _ in range(N)]

    # 동근이 위치 좌표
    sti, stj = map(int, input().split())
    # 빈 좌표 리스트 만들기
    arr = [[0]*(X+1) for _ in range(Y+1)]
    # 가운데 통과 못하니까 벽 B 채우기
    for i in range(1, Y):
        for j in range(1, X):
            arr[i][j] = 'B'
    # 동근이 위치 좌표상에 X 표시
    if sti == 1:    # 북쪽이면 행 인덱스 0
        arr[0][stj] = 'X'
    elif sti == 2:  # 남쪽이면 행 인덱스 Y
        arr[Y][stj] = 'X'
    elif sti == 3:  # 서쪽이면 열 인덱스 0
        arr[Y-stj+1][0] = 'X'
    elif sti == 4:  # 동쪽이면 열 인덱스 Y
        arr[Y-stj+1][X] = 'X'
    # pprint(arr)
    # print(shop_list)
    # print('='*50)
    for i, j in shop_list:
        if i == 1:
            arr[0][j] = 1
        elif i == 2:
            arr[Y][j] = 1
        elif i == 3:
            arr[Y-i][0] = 1
        elif i == 4:
            arr[Y-i][X] = 1

        pprint(arr)