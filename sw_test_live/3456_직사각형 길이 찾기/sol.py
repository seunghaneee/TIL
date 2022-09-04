import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))
    # print(num_list)
    num_list.sort()
    leng = [0] * 101
    for i in range(3):
        leng[num_list[i]] += 1
    # print(leng)
    for i in range(len(leng)):
        if leng[i] == 1 or leng[i] == 3:
            result = i

    print(f'#{tc} {result}')