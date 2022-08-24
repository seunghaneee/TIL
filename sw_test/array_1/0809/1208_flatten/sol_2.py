import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    # 박스의 최대 높이가 100이며
    # 각 높이별 박스를 카운트 하는 리스트에 담아서
    # 최대 높이와 최소 높이를 찾아준다.

    C = [0] * 101 #높이가 100 이기 때문에 0 ~ 100
    # 비교 할 최대값과 최소값 초기 설정
    h_max = 0
    h_min = 101

    for i in range(100):
        C[boxes[i]] += 1

        # 최대 높이 구하기
        if boxes[i] > h_max:
            h_max = boxes[i]
        if boxes[i] < h_min:
            h_min = boxes[i]

    # 덤프 횟수가 다 끝나거나 최대 최소값의 차이가 2 미만일 때 까지만 실행
    while N > 0 and h_max - h_min > 1:
        C[h_max] -= 1
        C[h_min] += 1
