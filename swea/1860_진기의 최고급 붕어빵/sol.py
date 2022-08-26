import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 예약 손님 N명 / 붕어빵 굽는 타임 M /  M초 동안 만들 수 있는 붕어빵 개수 K
    N, M, K = map(int, input().split())
    # 손님 도착 시간 동시에 도착해도 상관X
    arr = list(map(int, input().split()))

    # 우선 정렬해서 생각하자
    arr.sort()

    # 전체 사람(N명)중 K명이 M 시간 이내에 도착한다면 가능

    result = 'possible'
    for i in range(N):
        # 붕어빵은 가장 늦은 시간에 오는 사람의 시간 // M + 1만큼 구워야 된다.
        # 따라서 전체 구워지는 붕어빵 개수는 arr[-1] // M * K 이다.
        if (arr[i] // M) * K < i + 1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')




