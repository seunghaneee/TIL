import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))

    # 조망권이 확보된 총 세대수
    result = 0
    # 현재 위치 기준으로 탐색할 인덱스를 담은 리스트
    search_list = [-2, -1 , 1, 2]
    # 건물 시작 2개와 끝점 2개는 높이가 0이다.
    for i in range(2, N-2):
        # 현재 빌딩 위치를 기준으로 좌우 2개씩 확인
        h_max = 0
        for j in search_list:
            if building[i+j] > h_max:
                h_max = building[i+j]

        # 만약 현재 위치의 빌딩 높이가 양옆 2개의 빌딩 중 가장 높은 빌딩보다 높을 때
        # 결과값에 내 높이에서 양 옆 빌딩 중 가장 높은 빌딩의 높이를 뺀 값을 더해준다.
        if building[i] > h_max:
            result += building[i] - h_max
        # 만약 현재 위치의 빌딩 높이가 2칸 이내 빌딩중 최고높이보다 낮다면
        # 조망권을 가진 집이 없다.
        elif building[i] <= h_max:
            result += 0

    print(f'#{tc} {result}')
