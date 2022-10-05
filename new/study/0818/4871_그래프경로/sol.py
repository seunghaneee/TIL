import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1

    for w in range(1, V+1):
        if adjList[v][w] == 1 and visited[w] == 0:
            dfs(w)

T = int(input())

for tc in range(1, T+1):
    # V: 노드 개수, E: 간선 개수
    V, E = map(int, input().split())
    N = V + 1

    # 인접행렬 생성
    adjList = [[0] * N for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a][b] = 1
    S, G = map(int, input().split())    # S: 출발 노드, G: 도착 노드
    # print(adjList)
    visited = [0] * N
    dfs(S)
    print(visited[G])