import sys
sys.stdin = open('input.txt')

T = 11
# 버블 정렬을 활용한 리스트 정렬
def bubble(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

for tc in range(1, T+1):
    # dump 횟수
    dump = int(input())
    # 박스 높이 리스트
    array = list(map(int, input().split()))

    # 일단 아이디어는 정렬해놓고
    # 제일 높은데에서 제일 낮은데로 옮기기를 dump만큼 반복
    # 다시 정렬하고 반복
    # def 버블정렬 해놓고 쓰자!
    # 덤프 횟수 만큼 반복 혹은 최대 최소값의 차이가 2 미만이면 중지
    # count = 0
    for i in range(dump):
        bubble(array)
        array[-1] -=1
        array[0] += 1
        # count += 1

    bubble(array)
    max_h = array[-1]
    min_h = array[0]

    result = max_h - min_h
    # print(count, dump)
    print(f'#{tc} {result}')