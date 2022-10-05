# A도시에서 B도시로 가는 길이 존재하는지 찾는 알고리즘
import sys
sys.stdin = open('1219_input.txt')

def bfs(v, N, t):           # v 시작, N 마지막 정점, t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)     # 시작 정점 인큐
    visited[v] = 1  # 시작 정점 방문 표시
    while q:
        v = q.pop(0)
        if v == t:       # 내가 찾는 목표에 도착하면
            # return 1     # 목표발견
            return visited[99]  # 목표지점까지 거리
        for w in adjList[v]:    # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                # visited[w] = visited[v] + 1
                visited[w] = 1
    return 0
T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접 리스트 만들기
    adjList = [[] for _ in range(100)]      # 정점 개수 100개 (0~99)
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjList[a].append(b)        # 단방향
    # print(adjList)

    # bfs(0, 99, 99)  # 시작 정점, 마지막 정점 번호, 찾고자 하는 목표정점

    print(f'#{tc} {bfs(0, 99, 99)}')