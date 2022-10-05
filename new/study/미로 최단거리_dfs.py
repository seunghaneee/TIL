'''
3
5
11111
12001
10101
13001
11111
5
11111
12131
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
100000031
111111111

'''
def dfs(i, j, N):
    global answer
    if arr[i][j] == 3:
        answer += 1 # 경로의 수
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if arr[ni][nj] != 1 and visited[ni][nj] == 0:   # 벽(1)로 둘러쌓인 미로
                dfs(ni, nj, N)
        visited[i][j] = 0
        return
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
    answer = 0  # 경로의 수
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, N)
    print(answer)