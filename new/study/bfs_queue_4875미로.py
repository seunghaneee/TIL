# import sys
# sys.stdin = open('4875__input.txt')

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1   # 시작점 방문 표시
    while q:
        i, j = q.pop(0)
        # 3번인가?(목적지)
        if arr[i][j] == 3:
            # return 1
            return visited[i][j]  # 목적지까지 최단거리
        for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 경계 조건
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:   # 벽이 아니고 방문X
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # return 0
    return -1
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 미로크기 N x N
    arr = [list(map(int, input())) for _ in range(N)]
    # 2번에서 3번까지 경로가 존재하는가
    # 시작점 찾기
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작점
                sti = i
                stj = j
                break
        if sti != -1:
            break


    print(f'#{tc} {bfs(sti, stj, N)}')