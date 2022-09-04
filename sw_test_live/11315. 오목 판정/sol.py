import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(str, input())) for _ in range(N)]
    result = 'NO' #기본값 NO

    #우 하 오른쪽대각선\ 왼쪽대각선/
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            #o를 만나면
            if lst[i][j] == 'o':
                for d in range(4):
                    cnt = 1 #만났으니 기본값 1
                    newi = i + dx[d]
                    newj = j + dy[d]
                    #범위 내에 있고 우, 하, 대각선 중 이어지는 값이 o라면 cnt에 1씩 더해주기
                    while 0 <= newi < N and 0 <= newj < N and lst[newi][newj]=='o':
                        cnt += 1
                        newi = newi + dx[d]
                        newj = newj + dy[d]
                    #오목일때 YES로 바꾸기
                    if cnt >= 5:
                        result = 'YES'

    print("#{} {}".format(tc+1, result))