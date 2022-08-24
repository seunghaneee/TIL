import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 단조 증가하는 수 찾기 위해
    # A_i * A_j를 새로운 리스트로 만든다
    result = -1
    for i in range(N):
        for j in range(i+1, N):
            # 리스트에서 2개를 골라 곱하기
            new_number = numbers[i] * numbers[j]

            # 곱해진 수에서 각 자리수를 출력하여 단조인지 확인
            dan = False
            for k in range(len(str(new_number)) - 1):
                if int(str(new_number)[k + 1]) > int(str(new_number)[k]):
                    dan = True
            if dan == True:
                if result < new_number:
                    result = new_number

    print(f'#{tc} {result}')