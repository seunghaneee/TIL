import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    # 행, 렬, 대각선의 합 중에서 최대값만 출력하기

    # 행 계산
    row_sum_list = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += array[i][j]
        row_sum_list.append(total)
    max_row_sum = row_sum_list[0]
    for i in range(len(row_sum_list)):
        if max_row_sum < row_sum_list[i]:
            max_row_sum = row_sum_list[i]
    # print(max_row_sum)

    # 열 계산
    col_sum_list = []
    for j in range(100):
        total = 0
        for i in range(100):
            total += array[i][j]
        col_sum_list.append(total)
    max_col_sum = col_sum_list[0]
    for i in range(len(col_sum_list)):
        if max_col_sum < col_sum_list[i]:
            max_col_sum = col_sum_list[i]
    # print(max_col_sum)

    # 대각선 계산
    cross_1_list = []
    cross_2_list = []
    total_1, total_2 = 0, 0
    for j in range(100):
        total_1 += array[j][j]
        total_2 += array[j][100-j-1]
    cross_1_list.append(total_1)
    cross_2_list.append(total_2)
    max_cross_1_sum = cross_1_list[0]
    max_cross_2_sum = cross_2_list[0]

    for i in range(len(cross_1_list)):
        if max_cross_1_sum < cross_1_list[i]:
            max_cross_1_sum = cross_1_list[i]

    for i in range(len(cross_2_list)):
        if max_cross_2_sum < cross_2_list[i]:
            max_cross_2_sum = cross_2_list[i]

    result_list = [max_row_sum, max_col_sum, max_cross_1_sum, max_cross_2_sum]

    result = result_list[0]
    for i in range(len(result_list)):
        if result < result_list[i]:
            result = result_list[i]

    print(f'#{test_num} {result}')

