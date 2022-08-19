import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    result = 0
    # 시작 부분을 초기값으로 하기 위해 같은 인덱스끼리 곱해주면 된다.
    for i in range(min(len(Ai), len(Bj))):
        result += (Ai[i] * Bj[i])

    # 만약 N = 5, M = 3 이라면 2번 움직여야 하는데
    # 인덱스를 이동하기 위해 range(1, N-M+1) 해주면 2번 움직인다.
    # 하지만 N이 큰지 M이 큰지는 모르기 때문에 나눠서 생각한다.

    # Ai의 길이가 Bj의 길이보다 짧은 경우 Bj의 인덱스를 옮기며 계산을 해야한다.
    if N < M:
        for move_idx in range(1, M-N+1):
            sum = 0
            for idx in range(N): # Ai가 짧으므로 N회 계산하는데 Bj가 이동한다.
                sum += Ai[idx] * Bj[idx + move_idx]

                if sum > result:
                    result = sum
    print(result)


