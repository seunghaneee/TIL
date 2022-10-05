'''
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

def dfs(v):
    print(v)        # 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)



V, E = map(int, input().split())    # 마지막 정점번호, 간선 개수
N = V + 1   # 정점 개수

# 간선 개수와 경로를 보고 인접행렬 만들기
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N       # visited 생성(초기화)
dfs(0)