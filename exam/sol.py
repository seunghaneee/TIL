'''
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5

'''

T = int(input())

for tc in range(1, T+1):
    # N: 신입 사원 수
    # K_min: 각 반 최소 인원
    # K_max: 각 반 최대 인원
    N, K_min, K_max = map(int, input().split())
    # 각 어학성적
    numbers = list(map(int, input().split()))
    # 우선 정렬해서 생각하자.
    numbers.sort()
    # 기준점 리스트
    T_list = list(set(numbers))

    result = []
    # T1, T2 선정
    for j in range(len(T_list)-1):
        for k in range(j+1, len(T_list)):
            T_1 = T_list[j]
            T_2 = T_list[k]
            # 각 분반 리스트
            A = []
            B = []
            C = []
            # 전체 점수를 순회할 때
            for i in numbers:
                # A분반: T_2 이상 / B분반: T_1 이상 T_2 미만 / C분반: T_1 미만
                if i < T_1:
                    C.append(i)
                elif T_1 <= i < T_2:
                    B.append(i)
                elif i >= T_2:
                    A.append(i)

            # 각 A,B,C 리스트의 길이가 K_min 이상 K_max 이하여야 한다.
            if K_min <= len(A) <= K_max:
                if K_min <= len(B) <= K_max:
                    if K_min <= len(C) <= K_max:
                        result.append(max(len(A), len(B), len(C)) - min(len(A), len(B), len(C)))
    result.sort()
    # print(result)

    if len(result) == 0:
        total = -1
    else:
        total = result[0]
    print(f'#{tc} {total}')