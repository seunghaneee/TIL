import sys
sys.stdin = open('input.txt')

def dfs(n):
    # 출발지 n(0) 방문표시
    visited[n] = 1
    for w in range(1, 100):
        if adjList[n][w] == 1 and visited[w] == 0:
            dfs(w)

# bfs로 풀어보기
def bfs(v, N, t):   # 시작정점, 마지막 정점, 찾는 정점
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:
            return visited[99]
    for w in adjList[v]:
        if visited[v] == 0:
            q.append(w)
            visited[w] = visited[v] + 1

T = 10
for _ in range(1, T+1):
    # 테스트 케이스 번호, 간선 개수
    tc, E = map(int, input().split())
    # 간선 정보
    data = list(map(int, input().split()))

    visited = [0] * 100

    # 인접행렬 생성
    # adjList = [[0] * 100 for _ in range(100)]
    # for i in range(0, len(data), 2):
    #     adjList[data[i]][data[i+1]] = 1
    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = data[i*2], data[i*2+1]
    print(adjList)
    dfs(0)
    # 만약 99번을 방문했다면 visited[99]에 1이 들어가 있고 아니라면 0일 것이다.
    # print(f'#{tc} {visited[99]}')
    bfs(0, 99, 99)