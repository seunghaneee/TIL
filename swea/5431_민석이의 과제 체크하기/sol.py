import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 총 수강생수 N / 과제 제출한 사람수 K
    N, K = map(int, input().split())
    # 과제 제출한 사람 번호
    # 모든 수강생 번호는 1~N
    array = list(map(int, input().split()))

    # 과제를 제출하지 않은 사람 번호를 찾고 오름차순 정렬
    C = [0] * (N+1)
    for i in range(1, N+1):
        if i not in array:
            C[i] = i
    list_a = []
    for i in range(len(C)):
        if C[i] != 0:
            list_a.append(i)
    print(f'#{tc}', *list_a)