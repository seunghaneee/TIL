'''
YYYYYY
YNYNYNYNY
NNNNNNNNNN
YYYNYYYNYYYNYYNYYYYN
'''
import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    state = list(input())
    switch_count_list = [0] * (len(state)+1)
    for i in range(len(state)):
        if state[i] == 'Y':
            switch_count_list[i+1] += 1
            state[i] = 'N'

            for j in range(i+1, len(state)):
                if (j+1) % (i+1) == 0:
                    if state[j] == 'Y':
                        state[j] = 'N'
                    else:
                        state[j] = 'Y'

    print(f'#{tc} {sum(switch_count_list)}')