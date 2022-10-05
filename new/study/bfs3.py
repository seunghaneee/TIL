'''
3
5
11111
12001
10101
12001
11111
5
11111
12121
10111
10001
11111
9
111111111
120000001
101110101
100000101
111110101
101000101
101011101
100000021
111111111

'''

def bfs(N):
    visited = [[0] * N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 경계 조건
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:   # 벽이 아니고 방문X
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited[i][j] - 1
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 미로크기 N x N
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {bfs(N)}')

