import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    for i in range(N-8+1):
        for j in range(M-8+1):
            for a in range(i, i+8):
                for b in range(j, j+8):







