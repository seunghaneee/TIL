import sys
sys.stdin = open('in1.txt')

T = int(input())
# 델타 탐색
# +모양으로 잡을 때
# 상 하 좌 우
dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]

# x모양으로 잡을 때
# 좌상 우상 좌하 우하
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 각 노즐 위치에서 잡은 총량 리스트
    plus_catch = []
    x_catch = []
    # 노즐 놔둘 곳 찾기
    center_list = []
    for i in range(N):
        for j in range(N):
            center_i = i
            center_j = j
            center_list.append([i,j])

    for i, j in center_list:
        center_i = i
        center_j = j

        # 해당 노즐 위치에서 잡은 파리를 담을 리스트
        catch_1 = []        # +로 잡았을 때
        catch_2 = []        # x로 잡았을 때
        # + 모양 x모양 중 뿌렸을 때 최대로 잡을 수 있는 파리 구하기
        # + 모양으로 뿌렸을 때 중심점
        catch_1.append(arr[center_i][center_j])
        # x 모양으로 뿌렸을 때 중심점
        catch_2.append(arr[center_i][center_j])
        for i in range(1, M):
            for idx in range(4):
                # + 방향 델타 탐색
                ni_1 = center_i + dx1[idx] * i
                nj_1 = center_j + dy1[idx] * i
                # x 방향 델타 탐색
                ni_2 = center_i + dx2[idx] * i
                nj_2 = center_j + dy2[idx] * i
                # 경계조건
                if 0 <= ni_1 < N and 0 <= nj_1 < N:
                    catch_1.append(arr[ni_1][nj_1])
                if 0 <= ni_2 < N and 0 <= nj_2 < N:
                    catch_2.append(arr[ni_2][nj_2])

        # print(catch_1)
        # print(catch_2)
        plus_sum = sum(catch_1)
        x_sum = sum(catch_2)
        plus_catch.append(plus_sum)
        x_catch.append(x_sum)

    # print(plus_catch)
    # print(x_catch)

    total_list = plus_catch + x_catch
    # print(total_list)
    print(f'#{tc} {max(total_list)}')
