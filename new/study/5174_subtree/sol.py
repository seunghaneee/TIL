import sys
sys.stdin = open('sample_input.txt')

def f(n):
    if n == 0:      # 서브 트리가 비어 있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    # 정점 V
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(E):
        p, c = data[i*2], data[i*2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    print(f'#{tc} {f(N)}')