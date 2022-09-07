import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 버스 노선 개수
    N = int(input())
    # station[i][0]: 시작 정류장 번호, station[i][1]: 종점 정류장 번호
    station = [list(map(int, input().split())) for _ in range(N)]
    # P: 세어야 하는 정류장 개수
    P = int(input())
    # 정류장 번호
    Cj = []
    for _ in range(P):
        Cj.append(int(input()))

    P = [0] * 5001
    for i in range(len(station)):
        for j in range(station[i][0], station[i][1] + 1):
            P[j] += 1

    list_a = []
    for i in Cj:
        list_a.append(P[i])

    print(f'#{tc}', *list_a)


