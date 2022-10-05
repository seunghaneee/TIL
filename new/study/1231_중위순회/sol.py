import sys
sys.stdin = open('input.txt')

# 중위순회
def in_order(value):
    if value <= N:
        in_order(value * 2)
        result.append(tree[value])
        in_order(value * 2 + 1)


T = 10
for tc in range(1, T+1):
    # 트리가 갖는 정점의 총 수 N
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        temp = list(input().split())
        tree[i+1] = temp[1]

    result = []
    in_order(1)
    result_s = ''
    for i in result:
        result_s += i

    print(f'#{tc} {result_s}')

