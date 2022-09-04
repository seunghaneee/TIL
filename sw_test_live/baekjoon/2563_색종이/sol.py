import sys
sys.stdin = open('input.txt')
T = 1

for tc in range(1, T+1):
    # 색종이 개수
    N = int(input())
    # 좌표평면
    arr = [[0] * 100 for _ in range(100)]
    # 색종이 좌표 리스트
    paper_list = []
    for _ in range(N):
        # x: 세로축으로부터 거리(열 번호) y: 가로축으로부터 높이 (행 번호)
        x, y = map(int, input().split())

        for i in range(y, y+10):
            for j in range(x, x+10):
                arr[i][j] += 1
    count = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] >= 1:
                count += 1

    print(count)