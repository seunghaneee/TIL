import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))
    result = 0
    # 맨 왼쪽2 오른쪽2 은 건물 높이가 0이다.
    # 따라서 index 2 ~ N-3 번까지 시행하면서 확인하면 된다.
    for i in range(2, N-2):
        # 내 위치 기준 앞 뒤 2칸씩 계산하기 위해
        min_value = 256
        for j in range(5):
            # 내가 아니라면
            if j != 2:
                if building[i] - building[i - 2 + j] < min_value:
                    min_value = building[i] - building[i - 2 + j]

        if min_value > 0:
            result += min_value

    print(f"#{tc} {result}")