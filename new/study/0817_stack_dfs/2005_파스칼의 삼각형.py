import sys
sys.stdin = open('2005_input.txt')

T = int(input())
#memoization 활용
memo = [[1], [1, 1]]
for tc in range(1, T + 1):
    N = int(input())

    while len(memo) < N: # 준비된 줄보다 출력시킬 줄이 많으면 반복문을 수행
        l = len(memo)    # 현재 출력가능한 줄의 수

        # 다음 출력시킬 줄을 추가할 배열
        small_arr = [1]   # 왼쪽은 1을 붙인다.
        for i in range(0, l - 1):
            # 전 줄을 이용해[l-1] 다음 줄을 추가한다.
            small_arr.append(memo[l - 1][i] + memo[l - 1][i + 1])
        small_arr.append(1)     # 오른쪽에도 1을 붙인다.
        memo.append(small_arr)   # 배열에 추가해준다.

    print(f'#{tc}')
    for i in range(N):  # 원하는 줄의 개수를 출력한다.
        print(*memo[i])

# import sys
# sys.stdin = open('input.txt')
# T = int(input())
# # T = 10
# for tc in range(1, T + 1):
#     N = int(input())
#
#     # [1] 초기값 설정
#     arr = [[0] * (N + 1) for _ in range(N + 1)]
#     arr[1][1] = 1
#
#     for i in range(2, N + 1):
#         for j in range(1, i + 1):
#             arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
#
#     print(f'#{tc}')
#     for i in range(1, N + 1):
#         for j in range(1, i + 1):
#             print(arr[i][j], end=' ')
#         print()