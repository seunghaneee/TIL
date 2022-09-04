import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 과자 개수 N 사람 수 K
    N, K = map(int, input().split())

    # 받아간 과자 수를 카운트하기 위한 리스트
    check_list = [0] * K

    for i in range(N):
        check_list[0] += 1
        check_list.append(check_list.pop(0))

    result = max(check_list) - min(check_list)
    print(f'#{tc} {result}')