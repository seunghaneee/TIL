import sys
sys.stdin = open('input.txt')

T = 10

def bubble(boxes):
    for i in range(len(boxes) - 1, 0, -1):
        for j in range(0, i):
            if boxes[j] > boxes[j + 1]:
                boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
for tc in range(1, T+1):
    # 덤프 횟수 N
    N = int(input())
    # 박스 높이 list
    boxes = list(map(int, input().split()))

    # 가장 높이 있는 박스에서 하나씩 꺼내와서 가장 낮은 박스에 올려준다.
    # 하나 옮기면 count += 1

    # 정렬하고 젤 위에 박스를 젤 아래 박스로 하나 옮기고
    # 또다시 정렬하고를 N번 반복

    for i in range(N):
        bubble(boxes)
        boxes[-1] -= 1
        boxes[0] += 1

    bubble(boxes)

    # 최대 높이와 최소 높이의 차이를 구하는 문제
    result = boxes[-1] - boxes[0]

    print(f'#{tc} {result}')

    # 단점 : 정렬을 너무 많이 해서 시간이 너무 오래 걸린다.


