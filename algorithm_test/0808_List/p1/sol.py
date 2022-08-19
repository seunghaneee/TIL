import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    result = 0
    for i in range(N):
