import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    # array에서 M개씩 묶어서 합을 새로운 리스트에 담음
    new_list = []
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += array[j]
        new_list.append(total)
    # print(new_list)

#합계의 맥스값과 min 값을 구하는 공식을 이용한 풀이
    # 합계의 최대값을 구하기 위한 계산
    # max_sum = new_list[0]
    # for i in range(len(new_list)):
    #     if new_list[i] > max_sum:
    #         max_sum = new_list[i]
    #
    #
    # low_sum = new_list[0]
    # for i in range(len(new_list)):
    #     if new_list[i] < low_sum:
    #         low_sum = new_list[i]
    #
    # result = max_sum - low_sum
    #
    # print(f'#{tc} {result}')

# 버블정렬을 이용한 풀이
#     A = len(new_list)
#     for i in range(A-1, 0, -1):
#         for j in range(0, i):
#             if new_list[j] > new_list[j+1]:
#                 new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
#     max_sum = new_list[-1]
#     min_sum = new_list[0]
#
#     result = max_sum - min_sum
#     print(result)

# 카운팅정렬을 이용한 풀이
# 이 문제에서는 최대값과 최소값만 구하면 되기 때문에 카운팅 정렬은 비효율적이지만
# 일단 구해보자면 카운티을 세기 위한 리스트의 개수가 최대값만큼은 있어야 하기 때문에
# 미리 최대값을 구해보면
    A = len(new_list)
    count_C = 0
    for i in range(A):
        if new_list[i] > count_C:
            count_C = new_list[i]

    # 카운팅 리스트
    C = [0] * (count_C+1)
    # 정렬한 새로운 리스트
    B = [0] * A

    for i in range(A):
        C[new_list[i]] += 1

    # 개수를 세기 위해 앞의 값을 더해서 뒤에값에 추가
    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(A-1, -1, -1):
        C[new_list[i]] -= 1
        B[C[new_list[i]]] = new_list[i]
    print(B)