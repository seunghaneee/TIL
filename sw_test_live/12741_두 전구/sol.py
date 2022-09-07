import sys
sys.stdin = open('sample_input.txt')

T = int(input())
result = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    # 시작 시간: A, C 중 늦은 시간
    start_time = max(A, C)
    # 끝나는 시간: B, D 중 빠른 시간
    end_time = min(B, D)

    # print(start_time, end_time)

    count = 0
    if start_time < end_time:
        count = end_time - start_time


    result.append(count)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')