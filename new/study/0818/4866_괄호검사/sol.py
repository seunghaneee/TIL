import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()

    op = '{('
    cl = '})'
    stack = []

    result = 0
    for char in data:
        # 여는 괄호면
        if char in op:
            stack.append(char)
        # 닫는 괄호면
        if char in cl:
            # 만약 스택이 비었으면
            if not stack:
                break
            if char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                break
    # for문에 대한 else 조건
    else:
        if not stack:
            result = 1
    print(f'#{tc} {result}')