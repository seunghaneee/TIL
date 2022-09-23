'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
'''
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
'''

N = int(input())    # 정점 개수
E = N-1             # 간선 개수
arr = []
par = [0] * (N + 1)
for i in range(E):
    p, c = map(int, input().split())
    arr.append([p, c])
for i in arr:
    p, c = i[0], i[1]
    par[c] = p
result = par[2:]
for i in result:
    print(i)
