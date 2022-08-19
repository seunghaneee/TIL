import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    exam = list(map(int, input().split()))

    result = 0

    # 리스트에서 가장 큰 값부터 k개 합을 구해야 한다.
    # 따라서 정렬을 통해 리스트를 정렬하고 k개 추출하여 합을 구한다.

    # 버블정렬
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if exam[j] < exam[j+1]:
                exam[j], exam[j+1] = exam[j+1], exam[j]
    # print(exam)

    for i in range(K):
        result += exam[i]

    print(f'#{tc} {result}')