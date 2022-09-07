import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 버스가 정차하는 정류장 번호 담을 리스트
    stop_1 = []
    stop_2 = []
    stop_3 = []
    # 전체 노선 순회
    for i in range(N):
        start = arr[i][1]
        end = arr[i][2]
        # 1. 일반 버스라면
        if arr[i][0] == 1:
            stop_1.append(start)
            for i in range(start+1, end):
                stop_1.append(i)
            stop_1.append(end)

        # 2. 급행 버스라면
        elif arr[i][0] == 2:
            stop_2.append(start)
            if start % 2 == 0:
                for i in range(start+2, end, 2):
                    stop_2.append(i)

            elif start % 2 == 1:
                for i in range(start+2, end, 2):
                    stop_2.append(i)
            stop_2.append(end)

        # 3. 광역 급행버스라면
        elif arr[i][0] == 3:
            stop_3.append(start)
            # 시작이 짝수일 때
            if start % 2 == 0:
                for i in range(start+1, end):
                    # 4의 배수들만 넣어준다.
                    if i % 4 == 0:
                        stop_3.append(i)
            # 시작이 홀수일 때
            elif start % 2 == 1:
                for i in range(start+1, end):
                    # 3의 배수이면서 10의 배수가 아닌것들만 넣어준다.
                    if i % 3 == 0 and i % 10 != 0:
                        stop_3.append(i)
            stop_3.append(end)
    #
    print(stop_1)
    print(stop_2)
    print(stop_3)

    stop_list = stop_1 + stop_2 + stop_3
    # print(stop_list)
    # 각 정류장에 정차한 횟수 담을 count 리스트
    bus_stop =[0] * 1001
    for i in stop_list:
        bus_stop[i] += 1
    # print(bus_stop)

    print(f'#{tc} {max(bus_stop)}')

