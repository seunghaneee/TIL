def f(i, N, s, t):        # s: 이전까지의 합 / t: 찾고자 하는 값
    global answer
    global cnt
    cnt += 1
    # if s == t:  # 부분집합의 합이 t면
    #     answer += 1
    # elif i == N:    # 모든 원소가 고려된 경우
    #     return
    if i == N:
        if s == t:
            answer += 1
        return

    # 백트래킹
    # 원래 계산횟수(cnt)가 2047 이지만 백트래킹 해줌으로써 415번으로 감소
    elif s > t:    # 지금까지 합이 이미 목표치보다 크다면
        return

    else:
        f(i+1, N, s+A[i], t)    # A[i]가 포함된 경우
        f(i+1, N, s, t)         # A[i]가 포함되지 않은 경우

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# bit = [0] * 10
answer = 0
cnt = 0
f(0, 10, 0, 4)
print(answer, cnt)   # 부분집합 원소의 합이 10인 부분집합의 개수