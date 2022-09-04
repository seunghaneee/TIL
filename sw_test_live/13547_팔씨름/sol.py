import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    result = 'NO'
    # 팔씨름 15번 하여 8번 이상 이기면 면제
    while len(arr) < 15:
        arr.append('o')

    count = 0
    for i in arr:
        if i == 'o':
            count += 1
    if count >= 8:
        result = 'YES'

    print(f'#{tc} {result}')