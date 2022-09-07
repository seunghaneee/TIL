from pprint import pprint
# 델타 탐색 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# C: 가로길이 R: 세로길이
C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        arr[i][j] = [j+1, R-i]

idx = 0
# 시작점
i = R-1
j = 0
count = 1
while count <= C * R:
    count += 1
    ni = i + dx[idx]
    nj = j + dy[idx]

    if 0 <= ni < R and 0 <= nj < C and len(arr[i][j]) == 2:
        i = ni
        j = nj
    else:
        idx = (idx + 1) % 4

    if count-1 == K:
        print(*arr[i][j])
        break

if R*C < K:
    print(0)