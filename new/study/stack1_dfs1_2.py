# A~G -> 0~6
# 인접 행렬
# adjList = [         # 정점 번호, 각 정점에서 갈 수 있는 정점들
#     [1, 2],         # 0
#     [0, 3, 4],      # 1
#     [0, 4],         # 2
#     [1, 5],         # 3
#     [1, 2, 5],      # 4
#     [3, 4, 6],      # 5
#     [5]             # 6
# ]

def dfs(v, N):     # 정점 v에서 시작, 정점개수 N
    top = -1

    top += 1
    stack[top] = v      # 시작점
    print(v)            # 방문하는 정점 표시
    visited[v] = 1      # 방문표시 1    #시작점은 방문했으니까 1로 두고 시작

    while True:                     # 스택이 다 빌때까지 반복할 예정
        for w in adjList[v]:        # 각 정점에서 인접정점들을 가지고옴
            if visited[w] == 0:     # v의 인접 정점중 방문 안 한 정점 w가 있으면
                top += 1
                stack[top] = v      # 스택에 넣어주고
                v = w               # 해당 정점 방문
                print(v)            # 방문
                visited[w] = 1      # 방문표시 설정
                break

        else:                   # w가 없으면 (해당 정점에서 인접 정점이 없으면)
            if top != -1:       # 아직 스택에 값이 남아 있으면
                v = stack[top]  # 스택에서 꺼내주고 pop
                top -= 1
            else:               # 스택이 비어있으면
                break           # while문 종료


V, E = map(int, input().split())    # 마지막 정점번호, 간선 개수
N = V + 1   # 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
print(adjList)

visited = [0] * N       # visited 생성(초기화)
stack = [0] * N         # stack 생성

# dfs(0, N)       # 0번부터 시작하고 정점개수 7개
'''
0
1
3
5
4
2
6
'''

dfs(1, N)       # 1번부터 시작하고 정점개수 7개
'''
1
0
2
4
5
3
6
'''