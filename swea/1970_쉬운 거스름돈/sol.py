import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    money = int(input())
    # 돈의 종류가 10, 50, 100, 500, 1000, 5000, 10000, 50000
    # 8개가 있다.
    C = []
    exchange = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in exchange:
        if money >= i:
            C.append(money//i)
            money = money % i
        elif money < i:
            C.append(0)
    print(f'#{tc}')
    print(*C)

    # C = [0] * 8
    # while money > 0:
    #     if money >= 50000:
    #         C[0] = money // 50000
    #         money = money % 50000
    #     if money >= 10000:
    #         C[1] = money // 10000
    #         money = money % 10000
    #     if money >= 5000:
    #         C[2] = money // 5000
    #         money = money % 5000
    #     if money >= 1000:
    #         C[3] = money // 1000
    #         money = money % 1000
    #     if money >= 500:
    #         C[4] = money // 500
    #         money = money % 500
    #     if money >= 100:
    #         C[5] = money // 100
    #         money = money % 100
    #     if money >= 50:
    #         C[6] = money // 50
    #         money = money % 50
    #     if money >= 10:
    #         C[7] = money // 10
    #         money = money % 10
    #
    # print(f'#{tc}')
    # print(*C)