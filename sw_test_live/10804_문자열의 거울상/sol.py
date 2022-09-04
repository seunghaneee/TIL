import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = list(input())

    new_s = s[::-1]

    for i in range(len(new_s)):
        if new_s[i] == 'p':
            new_s[i] = 'q'
        elif new_s[i] == 'q':
            new_s[i] = 'p'
        elif new_s[i] == 'b':
            new_s[i] = 'd'
        elif new_s[i] == 'd':
            new_s[i] = 'b'
    result = ''
    for i in new_s:
        result += i
    print(f'#{tc} {result}')