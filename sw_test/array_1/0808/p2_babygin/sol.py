import sys
sys.stdin = open('input.txt')

T = int(input())
def check_babygin(numbers):
    # 0~9 까지의 숫자카드중 내가 받은 숫자들이 몇번 나왔는지 체크
    counter = [0] * 10 # counter = [0 for _ in range(10)]
    # babygin 이면 1, 아니면 0 반환
    is_babygin = 0

    # 내 카드 숫자 전체 순회하면서 카운팅
    for i in range(numbers):
        counter[i] += 1
for tc in range(1, T+1):
