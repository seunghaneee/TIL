import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input()))

    count = 0
    leng = []
    for i in number:
        if i == 1:
            count += 1
        elif i == 0:
            leng.append(count)
            count = 0
    leng.append(count)

    print(f'#{tc} {max(leng)}')
