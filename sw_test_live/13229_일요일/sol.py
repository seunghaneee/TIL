import sys
sys.stdin = open('sample_input.txt')

T = int(input())
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for tc in range(1, T+1):
    today = input()

    while today != day[0]:
        day.append(day.pop(0))
    count = 1

    for _ in range(1, len(day)+1):
        if day[1] != 'SUN':
            day.append(day.pop(0))
            count += 1
        else:
            break

    print(count)