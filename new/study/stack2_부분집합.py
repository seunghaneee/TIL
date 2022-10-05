def f(i,N):
    global answer
    global cnt
    cnt += 1
    if i == N:      # 채울칸의 인덱스번호와 개수가 같아지면
        # print(bit)
        s = 0   # 합을 구하기 위한 식
        for i in range(N):
            if bit[i]:
                # print(A[i], end = ' ')
                s += A[i]    # 합
        # print()
        if s == 10:    # 합이 10인 경우
            answer += 1 # 합이 10인 경우 카운트 증가
            # # 부분집합 원소의 합이 10인 경우 부분집합
            # for i in range(N):
            #     if bit[i]:
            #         print(A[i], end=' ')
            # print()
    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)
        # bit[i] = 1      # A[i]가 부분집합에 포함
        # f(i+1, N)
        # bit[i] = 0
        # f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer, cnt)   # 부분집합 원소의 합이 10인 부분집합의 개수