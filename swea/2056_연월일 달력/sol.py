import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    data = input()
    Y = data[0:4]
    M = data[4:6]
    D = data[6:8]

    if (int(M) in [1, 3, 5, 7, 8, 10, 12]) and (0 < int(D) < 32):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    elif (int(M) in [4, 6, 9, 11]) and (0 < int(D) < 31):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    elif int(M) == 2 and (0 < int(D) < 29):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    else:
        ans = '-1'
    print('#{} {}'.format(tc, ans))