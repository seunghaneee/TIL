import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 졸업요건 수업일수
    N = int(input())
    study_day = list(map(int, input().split()))

    # 수업은 하루만 들어도 졸업이어도 마지막날 수업이 있다면 최소 일주일은 있어야 한다.
    start_day = []
    min_day = N * 7
    for i in range(len(study_day)):
        if study_day[i] == 1:
            start_day.append(i)

    while True:
        for i in start_day:
            min_day = 0















