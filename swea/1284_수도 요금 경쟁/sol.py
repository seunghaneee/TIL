import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    price_A = P * W

    if W <= R:
        price_B = Q
    elif W > R:
        price_B = Q + (W-R)*S

    result = 0

    if price_A > price_B:
        result = price_B
    else:
        result = price_A

    print(f'#{tc} {result}')