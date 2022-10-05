import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []
    word = input()

    for char in word:
        # 스택이 비었으면 일단 스택에 넣기
        if not stack:
            stack.append(char)
        # 스택 가장 마지막에 들어간 문자와 현재문자가 같으면
        elif stack[-1] == char:
            # 스택에서 제거
            stack.pop()
        # 다르면
        else:
            stack.append(char)

    # print(stack)
    print(f'#{tc} {len(stack)}')