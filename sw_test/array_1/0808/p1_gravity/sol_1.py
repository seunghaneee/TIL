import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 상자들이 담겨 있는 array 인덱스 수
    N = int(input())
    # 각 인덱스에 상자가 몇칸씩 쌓여있는지 리스트로 받아온다.
    array = list(map(int, input().split()))

    # 최종 결과값은 가장 많은 낙차가 있는것을 반환해야함
    # 전체 낙차를 순회하기 위한 반복문 시행 후 가장 많은 낙차 result 구하기
    result = 0
    # 전체 순회는 인덱스 수 만큼 순회하면 된다.
    for i in range(N):
        # 다음 인덱스를 고려하지 않고 일단 최대 떨어질 수 있는 높이 구하기
        # 첫 번째 인덱스가 0이고 마지막 인덱스가 5라면 5칸 떨어지고 그 다음부터 1칸씩 줄어든다.
        max_h = N - (i+1)

        # print(max_h)
    # print('=========')
        # 만약 내 다음 인덱스(i+1)에 상자가 있다면 max_h는 줄어든다.
        for j in range(i+1, N):
            # 내 인덱스 다음번째를 순회했을 때 array의 크기가 나보다 크거나 같으면 max_h감소
            if array[i] <= array[j]:
                max_h -= 1

        # 최대 낙차값을 구하기 위해 max_h와 result를 비교하여 큰값을 result에 저장
        if max_h > result:
            result = max_h

    print(f'#{tc} {result}')