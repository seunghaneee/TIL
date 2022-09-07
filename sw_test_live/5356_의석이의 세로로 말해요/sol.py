`import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    a = 0
    for i in range(len(arr)):
        if a < len(arr[i]):
            # 최대 문자 길이
            a = len(arr[i])

    arr_list = [[''] * a for _ in range(5)]

    # print(arr_list)
    for i in range(5):
        for j in range(len(arr[i])):
                arr_list[i][j] = arr[i][j]
    # print(arr_list)

    # 세로로 읽기
    result_list = []
    for j in range(a):
        for i in range(len(arr_list)):
            result_list.append(arr_list[i][j])
    # print(result_list)
    result = ''
    for i in result_list:
        result += i
    print(f'#{tc} {result}')`